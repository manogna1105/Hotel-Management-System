document.addEventListener("DOMContentLoaded", () => {
  const checkin = document.getElementById("checkin");
  const checkout = document.getElementById("checkout");

  const today = new Date();
  const tomorrow = new Date();
  tomorrow.setDate(today.getDate() + 1);

  const formatDate = (date) => date.toISOString().split("T")[0]; // yyyy-mm-dd

  checkin.value = formatDate(today);
  checkout.value = formatDate(tomorrow);
});

// Scroll to search on Book Now
const bookBtn = document.querySelector(".hero .btn");
const searchSection = document.querySelector(".search-section");

document.querySelectorAll('.room-card button').forEach(btn => {
  btn.addEventListener('click', () => {
    alert('More details coming soon!');
  });
});