const backendUrl = "http://localhost:80/";


function loadBotStatus() {
    const xml = new XMLHttpRequest();
    xml.open("GET", backendUrl + "is_bot_running");
    let gotResponse = false;

    xml.onreadystatechange = () => {
        if (!gotResponse && xml.responseText) {
            const botActiveDiode = document.getElementById("bot-active-diode")
            const botActiveDiodeText = document.getElementById("bot-active-diode-text")

            if (xml.responseText === "true") {
                botActiveDiode.classList.remove("bg-red-600");
                botActiveDiode.classList.add("bg-green-600");

                botActiveDiodeText.innerHTML = "Running...";
            }
            else {
                botActiveDiode.classList.remove("bg-green-600");
                botActiveDiode.classList.add("bg-red-600");

                botActiveDiodeText.innerHTML = "Paused...";
            }

            gotResponse = true;
        }
    }

    xml.send();
}

window.onload = () => {
    setTimeout(loadBotStatus, 0);
}
