let display = document.getElementById("display");

function appendChar(char) {
    display.value += char;
}

function clearDisplay() {
    display.value = "";
}

async function calculate() {
    let expression = display.value;
    if (!expression) return;

    let response = await fetch("/calculate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ expression: expression })
    });

    let data = await response.json();
    if (data.result !== undefined) {
        display.value = data.result;
    } else {
        display.value = "Error";
    }
}