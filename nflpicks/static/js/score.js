
// get selected choice
function teamChoice(home, away, vs) {
    return {
        HomeWin: home,
        AwayWin: away,
        NoWin: vs,
    };
}

var choice = [
    { "make1": "Porsche", "model": "911S" },
    { "make2": "Mercedes-Benz", "model": "220SE" },
    { "make3": "Jaguar", "model": "Mark VII" }
];


window.onload = function () {
    // setup the button click
    document.getElementById("submit-btn").onclick = function () {
        sendData()
    };
}

function sendData() {
    // ajax the JSON to the server
    $.ajax({
        type: 'POST',
        url: "{{ url_for('index') }}",
        data: JSON.stringify(choice),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8'
    }).done(function (data) {
        console.log(data);
    });
    // stop link reloading the page
    event.preventDefault();
}
