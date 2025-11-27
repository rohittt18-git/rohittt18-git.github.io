const techBtn = document.getElementById("tech");
const closeTech = document.getElementById("closeTech");
const techSection = document.getElementById("technicalSection");
const homeSection = document.getElementById("homeSection");

// Open Technical Section
techBtn.addEventListener("click", () => {
    homeSection.style.filter = "blur(5px)";
    techSection.classList.add("active");
});

// Close Technical Section
closeTech.addEventListener("click", () => {
    techSection.classList.remove("active");
    setTimeout(() => {
        homeSection.style.filter = "none";
    }, 800);
});
// Mobile / touch toggle for flip