document.addEventListener("DOMContentLoaded", () => {
    let counter = 0;
    document.querySelector("#increment").onclick = () => {
        counter++;
        document.querySelector("h1").innerHTML = counter;
    };
    document.querySelector("#decrement").onclick = () => {
        counter--;  // Change this line from counter++ to counter--
        document.querySelector("h1").innerHTML = counter;
    };
});
