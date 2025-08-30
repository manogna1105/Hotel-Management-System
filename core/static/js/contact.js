document.getElementById('contactForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const firstName = document.getElementById('firstName').value.trim();
  const lastName = document.getElementById('lastName').value.trim();
  const email = document.getElementById('email').value.trim();
  const subject = document.getElementById('subject').value;
  const message = document.getElementById('message').value.trim();

  if (!firstName || !lastName || !email || !subject || !message) {
    alert("Please fill in all required fields.");
    return;
  }

  alert("Thank you! Your message has been sent.");
  this.reset();
});

  document.querySelectorAll('.faq-question').forEach(button => {
    button.addEventListener('click', () => {
      const item = button.parentElement;
      const isActive = item.classList.contains('active');

      // Close all other items
      document.querySelectorAll('.faq-item').forEach(el => {
        el.classList.remove('active');
        el.querySelector('.icon').textContent = '+';
      });

      // Toggle current
      if (!isActive) {
        item.classList.add('active');
        item.querySelector('.icon').textContent = '×';
      }
    });
  });


