// JavaScript for the Signup Form
document.addEventListener('DOMContentLoaded', () => {
    // Toggle password visibility
    const passwordFields = document.querySelectorAll('.password');
    const eyeIcon = document.querySelector('.eye-icon');
  
    if (eyeIcon) {
      eyeIcon.addEventListener('click', () => {
        passwordFields.forEach((field) => {
          const type = field.type === 'password' ? 'text' : 'password';
          field.type = type;
        });
        // Toggle eye icon class
        eyeIcon.classList.toggle('bx-hide');
        eyeIcon.classList.toggle('bx-show');
      });
    }
  
    // Form validation
    const form = document.querySelector('form');
    form.addEventListener('submit', (event) => {
      event.preventDefault(); // Prevent form submission for validation
      const role = form.querySelector('input[name="user-role"]:checked');
      const email = form.querySelector('input[type="email"]').value.trim();
      const password = passwordFields[0].value.trim();
      const confirmPassword = passwordFields[1].value.trim();
      const phone = form.querySelector('input[type="text"][placeholder="Mobile Number"]').value.trim();
  
      // Validation checks
      if (!role) {
        alert('Please select your role (Doctor or Patient).');
        return;
      }
  
      if (!email || !validateEmail(email)) {
        alert('Please enter a valid email address.');
        return;
      }
  
      if (!password || password.length < 6) {
        alert('Password must be at least 6 characters long.');
        return;
      }
  
      if (password !== confirmPassword) {
        alert('Passwords do not match.');
        return;
      }
  
      if (!phone || !validatePhoneNumber(phone)) {
        alert('Please enter a valid 10-digit mobile number.');
        return;
      }
  
      // If all validations pass, simulate form submission
      alert('Signup successful!');
      form.reset();
    });
  
    // Helper function to validate email
    function validateEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    }
  
    // Helper function to validate phone number
    function validatePhoneNumber(phone) {
      const phoneRegex = /^[0-9]{10}$/;
      return phoneRegex.test(phone);
    }
  });
  