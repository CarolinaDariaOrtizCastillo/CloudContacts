document.getElementById("contactForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();

    const res = await fetch("/api/add-contact", {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify({ name, email, phone })
    });

    const data = await res.json();
    const msg = document.getElementById("msg");

    if (data.saved) {
        msg.style.color = "green";
        msg.textContent = "Contacto guardado correctamente.";
        document.getElementById("contactForm").reset();
    } else {
        msg.style.color = "red";
        msg.textContent = data.error;
    }
});
