document.getElementById('mobile-menu').addEventListener('click', function () {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');

    const menuToggle = document.getElementById('mobile-menu');
    menuToggle.classList.toggle('change');
});
// JavaScript function to scroll to the top of the page
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'  // Optional, smooth scrolling
    });
}
  
// Show scroll-to-top button when user scrolls down 20px from the top
window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    var scrollButton = document.querySelector('.scroll-to-top');
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        scrollButton.style.display = "block";
    } else {
        scrollButton.style.display = "none";
    }
}

document.addEventListener('DOMContentLoaded', function(){
    const content = document.querySelector('.sect1');
    content.classList.add('loaded');
});

document.addEventListener('DOMContentLoaded', function(){
    const content = document.querySelector('.about');
    content.classList.add('loaded');
});

document.addEventListener('DOMContentLoaded', function(){
    const content = document.querySelector('.container_currency');
    content.classList.add('loaded');
});

document.addEventListener('DOMContentLoaded', function(){
    const content = document.querySelector('.shop');
    content.classList.add('loaded');
});

document.addEventListener('DOMContentLoaded', function(){
    const content = document.querySelector('.Goals');
    content.classList.add('loaded');
});

document.addEventListener('DOMContentLoaded', () => {
    const boxes = document.querySelectorAll('.container_benefit');

    const isInViewport = (element) => {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    };

    const handleScroll = () => {
        boxes.forEach(container_benefit => {
            if (isInViewport(container_benefit)) {
                container_benefit.classList.add('visible');
            }
        });
    };

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Initial check
});

function googleTranslateElementInit() {
    new google.translate.TranslateElement(
        {pageLanguage: 'en'},
        'google_translate_element'
    );
}
// Get the translate icon element
const translateIcon = document.getElementById('translate-icon');

// Add bounce animation
translateIcon.addEventListener('mouseover', () => {
translateIcon.style.animation = 'bounce 0.5s infinite alternate';
});

// Reset animation when mouse leaves
translateIcon.addEventListener('mouseleave', () => {
translateIcon.style.animation = '';
});
