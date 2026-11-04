document.querySelectorAll(".hero, .clients-hero, .proj-hero").forEach((hero) => {
  const backgroundImage = getComputedStyle(hero).backgroundImage;
  const imageMatch = backgroundImage.match(/url\(([^)]+)\)/);

  if (imageMatch) {
    hero.style.setProperty("--hero-image", `url(${imageMatch[1]})`);
    hero.style.backgroundImage = "none";
  }
});

if (document.querySelector(".hero, .clients-hero, .proj-hero")) {
  document.body.classList.add("hero-nav-layout");

  const contactLink = document.querySelector(".header .navbar-nav .nav-item:last-child .nav-link");

  if (contactLink && contactLink.getAttribute("href")?.includes("contact.html")) {
    contactLink.textContent = "Connect with us";

    const arrow = document.createElement("span");
    arrow.className = "hero-nav-arrow";
    arrow.setAttribute("aria-hidden", "true");
    arrow.textContent = "↗";
    contactLink.append(arrow);
  }
}
