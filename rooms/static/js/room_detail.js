document.addEventListener('DOMContentLoaded', function () {
    const today = new Date();
    const tomorrow = new Date(today);
    tomorrow.setDate(today.getDate() + 1);

    // Format date to YYYY-MM-DD
    const formatDate = (date) => {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
    };

    const checkInInput = document.querySelector('.booking-box input[name="check_in"]');
    const checkOutInput = document.querySelector('.booking-box input[name="check_out"]');

    if (checkInInput) checkInInput.value = formatDate(today);
    if (checkOutInput) checkOutInput.value = formatDate(tomorrow);
});