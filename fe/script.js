const URL = "http://localhost:8000/api/v1/test/"
var url = "url"

document.getElementById("form-img").addEventListener("submit", (e) => {
    e.preventDefault()
    // event.stopImmediatePropagation()
    onFormSubmit()
});

document.getElementById("btn-cap").addEventListener("click", (e) => {
    e.preventDefault()
    onFormSubmit()
    // capture()
}) 

async function onFormSubmit() {
    headers = {
        "Content-type": "application/json"
    }
    body = JSON.stringify(await capture())

    fetch(URL,
        {
            method: "POST",
            headers: headers,
            body: body
        })
        .then((response) => {
            console.log(response)
            if (response.ok) {
                console.log("then1")
                return response.json()
            }
        })
        .then((data) => {
            console.log("then2")
            console.log(data)
        })
        .catch((error) => {
            // alert("Error occured!")
            alert(error.stack)
            console.log(error)
        })
        .finally(() => {
            alert("???")
        })
}

function capture() {
    return html2canvas(document.body)
        .then((canvas) => {
            var c = document.getElementById("cap-img-canvas").getContext("2d")
            c.drawImage(canvas, 0, 0)
            return canvas.toDataURL("image/png")
        })
        .catch((err) => {
            alert("Error occured!")
            console.log(err)
        });
}