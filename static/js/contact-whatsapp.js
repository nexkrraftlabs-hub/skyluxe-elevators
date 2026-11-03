const WHATSAPP_NUMBER = "917275746520";

document.querySelectorAll(".js-whatsapp-form").forEach((form) => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();

    if (!form.reportValidity()) {
      return;
    }

    const formData = new FormData(form);
    const message = [
      "New inquiry from Skyluxe Elevators website",
      "",
      `Name: ${formData.get("name")}`,
      `Phone: ${formData.get("phone")}`,
      `Email: ${formData.get("email")}`,
      `City: ${formData.get("city") || "Not provided"}`,
      `Message: ${formData.get("message")}`,
    ].join("\n");

    window.location.href = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
  });
});
