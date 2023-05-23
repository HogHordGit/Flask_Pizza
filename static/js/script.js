// Скрипт для плавной прокрутки
const anchors = document.querySelectorAll('.slow-scroll');

for (let anchor of anchors) {
    anchor.addEventListener("click", (event) => {
        event.preventDefault();
        const blockID = anchor.getAttribute("href");
        document.querySelector("" + blockID).scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    });
}