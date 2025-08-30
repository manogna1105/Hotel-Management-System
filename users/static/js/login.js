function switchRole(role) {
    document.getElementById('roleInput').value = role;
    const tabs = document.querySelectorAll('.tab');
    tabs.forEach(tab => tab.classList.remove('active'));

    if (role === 'guest') {
      tabs[0].classList.add('active');
    } else {
      tabs[1].classList.add('active');
    }
  }