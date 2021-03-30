const backendUrl = "http://localhost:80/";


function loadDiode() {
    const xml = new XMLHttpRequest();
    xml.open("GET", backendUrl + "is_bot_running");
    let gotResponse = false;

    xml.onreadystatechange = () => {
        if (!gotResponse) {
            document.getElementById("bot-active-diode").style.backgroundColor = xml.responseText === "true" ? "green" : "red";
            document.getElementById("bot-active-diode-text").innerHTML = xml.responseText === "true" ? "Running..." : "Paused...";

            if (xml.responseText) {
                gotResponse = true;
            }
        }
    }

    xml.send();
}

window.onload = () => {
    setTimeout(loadDiode, 0);
    const loadingDiodeIntervalId = setInterval(() => {
        loadDiode();
    }, 5000);
}