const slides = document.querySelectorAll(".hero-slide");
const prevButton = document.getElementById("prev-slide");
const nextButton = document.getElementById("next-slide");
const pauseButton = document.getElementById("pause-slider");
const counter = document.getElementById("slide-counter");

if (slides.length > 0 && prevButton && nextButton && pauseButton && counter) {

    let currentSlide = 0;
    let timer = null;

    function showSlide(index) {
        slides[currentSlide].classList.remove("active");

        currentSlide = (index + slides.length) % slides.length;

        slides[currentSlide].classList.add("active");

        counter.textContent =
            String(currentSlide + 1).padStart(2, "0") +
            " / " +
            String(slides.length).padStart(2, "0");
    }

    nextButton.addEventListener("click", function () {
        showSlide(currentSlide + 1);
    });

    prevButton.addEventListener("click", function () {
        showSlide(currentSlide - 1);
    });

    function startSlider() {
        clearInterval(timer);

        timer = setInterval(function () {
            showSlide(currentSlide + 1);
        }, 5000);

        pauseButton.textContent = "Пауза";
    }

    function stopSlider() {
        clearInterval(timer);
        timer = null;
        pauseButton.textContent = "Старт";
    }

    pauseButton.addEventListener("click", function () {
        if (timer === null) {
            startSlider();
        } else {
            stopSlider();
        }
    });

    showSlide(0);

    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        stopSlider();
    } else {
        startSlider();
    }
}