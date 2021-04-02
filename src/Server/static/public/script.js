const backendUrl = "http://localhost:80/";


function loadBotStatus() {
    console.log("Loading bot status...");

    const xml = new XMLHttpRequest();
    xml.open("GET", backendUrl + "is_bot_running");
    let gotResponse = false;

    xml.onreadystatechange = () => {
        if (!gotResponse) {
            console.log("Got response: " + xml.responseText);

            const botActiveDiode = document.getElementById("bot-active-diode")
            const botActiveDiodeText = document.getElementById("bot-active-diode-text")

            if (xml.responseText === "true") {
                console.log("Bot is running...");

                botActiveDiode.classList.remove("bg-red-600");
                botActiveDiode.classList.add("bg-green-600");

                botActiveDiodeText.innerHTML = "Running...";
            }
            else if (xml.responseText) {
                console.log("Bot isn't running...");

                botActiveDiode.classList.remove("bg-green-600");
                botActiveDiode.classList.add("bg-red-600");

                botActiveDiodeText.innerHTML = "Paused...";
            }

            if (xml.responseText) {
                gotResponse = true;
            }
        }
    }

    xml.send();
}

window.onload = () => {
    setTimeout(loadBotStatus, 0);
}
