// rooms.js

document.addEventListener("DOMContentLoaded", () => {
    // Set default check-in/check-out dates
    const checkin = document.getElementById("checkin");
    const checkout = document.getElementById("checkout");
  
    const today = new Date();
    const tomorrow = new Date();
    tomorrow.setDate(today.getDate() + 1);
  
    const formatDate = (date) => date.toISOString().split("T")[0];
    if (checkin && checkout) {
      checkin.value = formatDate(today);
      checkout.value = formatDate(tomorrow);
    }
  
    // Price range slider logic
    const priceSlider = document.getElementById("maxPrice");
    const priceValue = document.getElementById("priceValue");
  
    if (priceSlider && priceValue) {
      priceValue.textContent = `₹ ${priceSlider.value}`;
      priceSlider.addEventListener("input", () => {
        priceValue.textContent = `₹ ${priceSlider.value}`;
      });
    }
  
    // View Details button placeholder logic
    document.querySelectorAll('.room-card button').forEach(btn => {
      btn.addEventListener('click', () => {
        alert('More details coming soon!');
      });
    });
  
    // Filter form logic
    const filterForm = document.getElementById("filterForm");
    const roomCards = document.querySelectorAll(".room-card");
  
    filterForm.addEventListener("submit", (e) => {
      e.preventDefault();
  
      const maxPrice = parseInt(priceSlider.value);
  
      const selectedTypes = Array.from(
        document.querySelectorAll("input[name='room_type']:checked")
      ).map(input => input.value.trim().toLowerCase());
  
      const selectedAmenities = Array.from(
        document.querySelectorAll("input[name='amenities']:checked")
      ).map(input => input.value.trim().toLowerCase());
  
      const selectedGuests = document.querySelector("input[name='guests']:checked")?.value;
  
      roomCards.forEach(card => {
        const type = card.dataset.type?.trim().toLowerCase();
        const price = parseInt(card.dataset.price);
        const guests = parseInt(card.dataset.guests);
        const amenities = card.dataset.amenities?.toLowerCase().split(',').filter(Boolean) || [];
  
        const matchPrice = price <= maxPrice;
        const matchType = selectedTypes.length === 0 || selectedTypes.includes(type);
        const matchAmenities = selectedAmenities.every(amenity => amenities.includes(amenity));
  
        let matchGuests = true;
        if (selectedGuests === "1-2") matchGuests = guests >= 1 && guests <= 2;
        else if (selectedGuests === "3-4") matchGuests = guests >= 3 && guests <= 4;
        else if (selectedGuests === "5+") matchGuests = guests >= 5;
  
        if (matchPrice && matchType && matchAmenities && matchGuests) {
          card.style.display = "block";
        } else {
          card.style.display = "none";
        }
      });
    });
  
    // ✅ Reset Filter Button functionality
    const resetBtn = document.createElement("button");
    resetBtn.textContent = "Reset Filters";
    resetBtn.type = "button";
    resetBtn.className = "filter-btn";
    filterForm.appendChild(resetBtn);
  
    resetBtn.addEventListener("click", () => {
      // Reset all inputs
      filterForm.reset();
      priceValue.textContent = `₹ ${priceSlider.value}`;
  
      // Show all rooms
      roomCards.forEach(card => {
        card.style.display = "block";
      });
    });
  });
  