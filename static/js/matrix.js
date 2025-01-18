const canvas = document.getElementById("matrix");
const ctx = canvas.getContext("2d");

// Configurar o canvas
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const characters = "01";
const fontSize = 16;
const columnWidth = fontSize + 2;
const columns = Math.floor(canvas.width / columnWidth);
const drops = Array.from({ length: columns }, () => Math.random() * canvas.height);

function drawMatrix() {
    ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.font = `${fontSize}px Courier New`;

    for (let i = 0; i < columns; i++) {
        const char = characters[Math.floor(Math.random() * characters.length)];
        const x = i * columnWidth;
        const y = drops[i] * fontSize;

        ctx.fillStyle = "#00ff00";
        ctx.fillText(char, x, y);

        if (y > canvas.height && Math.random() > 0.975) {
            drops[i] = 0;
        }

        drops[i]++;
    }
}

window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

function animate() {
    drawMatrix();
    requestAnimationFrame(animate);
}
animate();
