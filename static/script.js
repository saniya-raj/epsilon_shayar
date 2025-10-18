// 🌸 Gentle animation for page load
document.addEventListener("DOMContentLoaded", () => {
    const body = document.querySelector("body");
    body.style.opacity = 0;
    body.style.transition = "opacity 1.5s";
    setTimeout(() => {
        body.style.opacity = 1;
    }, 100);
});
// 🌸 Floating quote
const quotes = [
  "“Poetry is when an emotion has found its thought.” – Robert Frost",
  "“Phool to phool hai ankho se gire rehte hai ,” – Anonymous",
  "“Kante bekar ki hifazat me lage rehte hai” – Anonymous",
  "“Jadatar phoolo me psnd sbko phool-e-gulab ataa hai”",
  "“Aur exam ke time yaad sbko syllabus-e-kitaab aata hai.”",
  "“Let your pen be your voice, and your heart the ink.”"
];

window.onload = () => {
  const quoteBox = document.createElement("div");
  quoteBox.textContent = quotes[Math.floor(Math.random() * quotes.length)];
  quoteBox.style.position = "fixed";
  quoteBox.style.bottom = "20px";
  quoteBox.style.right = "20px";
  quoteBox.style.background = "rgba(255,255,255,0.9)";
  quoteBox.style.padding = "12px 18px";
  quoteBox.style.borderRadius = "10px";
  quoteBox.style.boxShadow = "0 0 10px rgba(0,0,0,0.2)";
  quoteBox.style.fontFamily = "'Poppins', sans-serif";
  quoteBox.style.color = "#b22222";
  quoteBox.style.fontSize = "14px";
  quoteBox.style.maxWidth = "300px";
  quoteBox.style.animation = "fadeIn 2s ease";
  document.body.appendChild(quoteBox);
  setTimeout(() => quoteBox.remove(), 10000);
};

// 🌿 Typewriter effect for the header title
const title = document.querySelector("header h1");
if (title) {
    const text = title.textContent;
    title.textContent = "";
    let i = 0;
    function typeWriter() {
        if (i < text.length) {
            title.textContent += text.charAt(i);
            i++;
            setTimeout(typeWriter, 100);
        }
    }
    typeWriter();
}

// 🖋️ Confirm before submitting a poem
const form = document.querySelector("form");
if (form) {
    form.addEventListener("submit", (e) => {
        const confirmSubmit = confirm("Do you want to submit it?");
        if (!confirmSubmit) {
            e.preventDefault();
        }
    });
}
function likeVerse(button) {
    const card = button.closest('.poem-card'); // find the card of the clicked button
    const countElem = card.querySelector('.like-count');
    let count = parseInt(countElem.textContent);
    count++;
    countElem.textContent = count;
}

function dislikeVerse(button) {
    const card = button.closest('.poem-card');
    const countElem = card.querySelector('.like-count');
    let count = parseInt(countElem.textContent);
    if(count > 0) count--; // don't allow negative likes
    countElem.textContent = count;
}
// 💫 Hover glow effect on poem cards
const cards = document.querySelectorAll(".poem-card");
cards.forEach(card => {
    card.addEventListener("mouseenter", () => {
        card.style.boxShadow = "0 0 15px rgba(178,34,34,0.6)";
        card.style.transform = "scale(1.05)";
        card.style.transition = "all 0.3s";
    });
    card.addEventListener("mouseleave", () => {
        card.style.boxShadow = "0 0 5px rgba(0,0,0,0.2)";
        card.style.transform = "scale(1)";
    });
});
