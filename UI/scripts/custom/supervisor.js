document.getElementById('staffEmail').addEventListener('change', function() {
    var email = this.value;
    if(email.endsWith('@staff.msu.ac.zw')) {
      // Email is valid
      console.log('Valid email address.');
    } else {
      // Email is invalid
      console.error('Invalid email address. It must end with @staff.msu.ac.zw');
      // Clear the invalid email
      this.value = '';
    }
  });