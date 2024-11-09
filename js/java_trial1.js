// JAVASCRIPT - TRIAL 1) - DELIVERY #4 

// STEP 1) - Implement Default Picture

document.querySelectorAll('img').forEach(img => {
    img.onerror = function() {
      this.onerror = null; // Prevents infinite loop if default image missing
      
      // IMPORTANT: If the path is ../images/profiles.. the image does load, but like this it works. 
      // Also changed the default picture with one downloaded from Google, because I had some problems with the one given. 
      this.src = 'images/profiles/default_image_2.jpg';
      this.alt = ""
    // to check if the image now works
      console.log("Hi")
    };
  });

// ---------------------------------------------
// STEP 2) Copyright sentence with Javascript
// target element with ID = currentYear 
// use newDate to get the current year 
document.getElementById("currentYear").textContent = new Date().getFullYear();

// ---------------------------------------------
// STEP 3) - Form in index.html to have the button Send to show up a message
// 
document.getElementById("ContactForm").onsubmit = function(event) {
  event.preventDefault(); // Prevent the form from submitting normally

  // Sending a feedback after clicking on Send button 
  alert("Thank you for contacting us!"); 
};

// ----------------------------------------------
// STEP 4) - Implement some Javascript libraries
// Using the Vanilla-tilt Library
// Used the same code given in the website (check SOIs in the report)

VanillaTilt.init(document.querySelector(".section_tilt_card"), {
  max:15, 
  speed:400
})

VanillaTilt.init(document.querySelectorAll(".section_tilt_card"));

// ----------------------------------------------


