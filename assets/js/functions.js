// Responsible for animation on landing page

document.addEventListener('DOMContentLoaded', function() {
    const options = {
      root: null, // Use the viewport as the container
      rootMargin: '0px',
      threshold: 0.1 // Trigger when at least 10% of the element is in the viewport
    };
  
    const callback = (entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Add the appropriate animation class
          if (entry.target.classList.contains('slide-in-left')) {
            entry.target.classList.add('slide-in-from-left');
          } else if (entry.target.classList.contains('slide-in-right')) {
            entry.target.classList.add('slide-in-from-right');
          } else if (entry.target.classList.contains('slide-in-bottom')) {
            entry.target.classList.add('slide-in-from-bottom');
          }
          observer.unobserve(entry.target); // Stop observing once the animation is triggered
        }
      });
    };
  
    const observer = new IntersectionObserver(callback, options);
  
    const listItems = document.querySelectorAll('.animated-list li');
    listItems.forEach((item, index) => {
      if (index === 0) {
        item.classList.add('slide-in-left');
      } else if (index === 1) {
        item.classList.add('slide-in-right');
      } else if (index === 2) {
        item.classList.add('slide-in-bottom');
      }
      observer.observe(item);
    });
  });

// Onscroll function on navbar
document.addEventListener('DOMContentLoaded', function () {
    window.onscroll = function () {
        myFunction();
    };

    function myFunction() {
        var navbar = document.querySelector('.navbar');
        var linksBarHeight = document.querySelector('.links-bar').offsetHeight;

        if (window.scrollY > linksBarHeight) {
            navbar.classList.add('fixed-navbar');
        } else {
            navbar.classList.remove('fixed-navbar');
        }
    }
});

// function for changing images on hero

let heroBackgrounds = document.querySelectorAll(".background");

let currentIndex = 0;

function changeBackground() {
  heroBackgrounds[currentIndex].classList.remove("showing");

  currentIndex++; //go to the next image 

  if (currentIndex >= heroBackgrounds.length) {
    currentIndex = 0;
  }

  heroBackgrounds[currentIndex].classList.add("showing");

}

setInterval(changeBackground, 3000);