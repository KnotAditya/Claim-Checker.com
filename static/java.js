document.addEventListener("DOMContentLoaded", function() {
    var elements = Array.from(document.querySelectorAll("*")); // Convert NodeList to Array for sorting

    // Sort elements by their vertical position from the top of the document
    elements.sort(function(a, b) {
        return a.getBoundingClientRect().top - b.getBoundingClientRect().top;
    });

    var index = 0;

    // Function to apply fade-in effect with a delay based on element's position
    function fadeIn(element, delay) {
        setTimeout(function() {
            var opacity = 0;
            var interval = setInterval(function() {
                if (opacity < 1) {
                    opacity += 0.05;
                    element.style.opacity = opacity;
                } else {
                    clearInterval(interval);
                }
            }, 50);
        }, delay);
    }

    // Apply the fade-in effect to each element with increasing delay
    elements.forEach(function(element, idx) {
        fadeIn(element, idx * 25); // Increase delay for each subsequent element
    });

    // Toggle responsive menu (for the hamburger icon)
    document.getElementById('hamburger-icon').addEventListener('click', function() {
        var navigation = document.getElementById("menu");
        if (navigation.className === "topnav") {
            navigation.className += " responsive";
        } else {
            navigation.className = "topnav";
        }
    });
});
