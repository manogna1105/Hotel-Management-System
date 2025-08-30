document.addEventListener("DOMContentLoaded", () => {
    const serviceCheckboxes = document.querySelectorAll('input[name="service_ids"]');
    const packageCheckboxes = document.querySelectorAll('input[name="package_ids"]');
    const roomInputs = document.querySelectorAll('.room-qty');
    const totalDisplay = document.getElementById("total");
  
    const roomInput = document.getElementById("roomInput");
    const serviceInput = document.getElementById("serviceInput");
    const packageInput = document.getElementById("packageInput");
    const totalInput = document.getElementById("totalInput");
  
    function calculateTotal() {
      let total = 0;
      const selectedRooms = [];
      const selectedServices = [];
      const selectedPackages = [];
  
      // Rooms
      roomInputs.forEach(input => {
        const qty = parseInt(input.value) || 0;
        const price = parseFloat(input.dataset.price);
        const roomId = input.dataset.roomId;
  
        if (qty > 0) {
          total += qty * price;
          selectedRooms.push(`${roomId}:${qty}`); // Example: 2:3 = Room ID 2, Quantity 3
        }
      });
  
      // Services
      serviceCheckboxes.forEach(cb => {
        if (cb.checked) {
          selectedServices.push(cb.value);
          total += parseFloat(cb.dataset.price);
        }
      });
  
      // Packages
      packageCheckboxes.forEach(cb => {
        if (cb.checked) {
          selectedPackages.push(cb.value);
          total += parseFloat(cb.dataset.price);
        }
      });
  
      // Set values
      totalDisplay.textContent = total.toFixed(2);
      roomInput.value = selectedRooms.join(',');
      serviceInput.value = selectedServices.join(',');
      packageInput.value = selectedPackages.join(',');
      totalInput.value = total.toFixed(2);
    }
  
    // Event Listeners
    [...roomInputs].forEach(input => input.addEventListener('input', calculateTotal));
    [...serviceCheckboxes].forEach(cb => cb.addEventListener('change', calculateTotal));
    [...packageCheckboxes].forEach(cb => cb.addEventListener('change', calculateTotal));
  
    calculateTotal(); // Initial calculation
  });
  