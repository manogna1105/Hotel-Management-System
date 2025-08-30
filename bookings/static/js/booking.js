document.addEventListener("DOMContentLoaded", () => {
  const roomInputs = document.querySelectorAll('.room-qty');
  const serviceCheckboxes = document.querySelectorAll('input[name="service_ids"]');
  const packageCheckboxes = document.querySelectorAll('input[name="package_ids"]');
  const totalDisplay = document.getElementById("total");

  const roomInput = document.getElementById("roomInput");
  const serviceInput = document.getElementById("serviceInput");
  const packageInput = document.getElementById("packageInput");
  const totalInput = document.getElementById("totalInput");

  const checkIn = document.getElementById("check-in");
  const checkOut = document.getElementById("check-out");
  const hiddenCheckIn = document.getElementById("hidden_checkin");
  const hiddenCheckOut = document.getElementById("hidden_checkout");

  const formatDate = (date) => {
    const year = date.getFullYear();
    const month = ("0" + (date.getMonth() + 1)).slice(-2);
    const day = ("0" + date.getDate()).slice(-2);
    return `${year}-${month}-${day}`;
  };

  const today = new Date();
  const tomorrow = new Date();
  tomorrow.setDate(today.getDate() + 1);

  checkIn.value = formatDate(today);
  checkOut.value = formatDate(tomorrow);

  function selectMethod(method) {
    document.getElementById('payment-method').value = method;

    document.querySelectorAll('.payment-btn').forEach(btn => {
      btn.classList.remove('selected');
    });

    const selectedButton = [...document.querySelectorAll('.payment-btn')].find(btn => btn.innerText.includes(method));
    if (selectedButton) selectedButton.classList.add('selected');

    const cardFields = document.getElementById('credit-card-fields');
    if (method === 'Credit Card') {
      cardFields.style.display = 'block';
    } else {
      cardFields.style.display = 'none';
    }
  }

  window.selectMethod = selectMethod;

  function calculateTotal() {

    if (new Date(checkOut.value) < new Date(checkIn.value)) {
      alert("Check-out date must be after check-in date.");
      return;
    }

    let total = 0;
    let selectedRooms = [];
    let selectedServices = [];
    let selectedPackages = [];

    const days = Math.max(1, Math.ceil((new Date(checkOut.value) - new Date(checkIn.value)) / (1000 * 60 * 60 * 24)));

    roomInputs.forEach(input => {
      const qty = parseInt(input.value) || 0;
      const price = parseFloat(input.dataset.price);
      const roomId = input.dataset.roomId;

      if (qty > 0) {
        selectedRooms.push(`${roomId}:${qty}`);
        total += qty * price * days;
      }
    });

    serviceCheckboxes.forEach(cb => {
      if (cb.checked) {
        selectedServices.push(cb.value);
        total += parseFloat(cb.dataset.price);
      }
    });

    packageCheckboxes.forEach(cb => {
      if (cb.checked) {
        selectedPackages.push(cb.value);
        total += parseFloat(cb.dataset.price);
      }
    });

    totalDisplay.textContent = total.toFixed(2);
    roomInput.value = selectedRooms.join(',');
    serviceInput.value = selectedServices.join(',');
    packageInput.value = selectedPackages.join(',');
    totalInput.value = total.toFixed(2);

    hiddenCheckIn.value = checkIn.value;
    hiddenCheckOut.value = checkOut.value;
  }

  roomInputs.forEach(input => input.addEventListener('input', calculateTotal));
  serviceCheckboxes.forEach(cb => cb.addEventListener('change', calculateTotal));
  packageCheckboxes.forEach(cb => cb.addEventListener('change', calculateTotal));
  checkIn.addEventListener('change', calculateTotal);
  checkOut.addEventListener('change', calculateTotal);

  calculateTotal();
});
