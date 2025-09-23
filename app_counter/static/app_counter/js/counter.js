 document.addEventListener("DOMContentLoaded", () => {
    console.log("Счетчик инициализирован");

 fetch(
    'http://127.0.0.1:8000/api/counter/increase/',
    {
        method: 'post',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Authorization': 'Token ...'
        },
        body: ""
    }
)
.then(response => response.json())
.then(res => alert(JSON.stringify(res)))
