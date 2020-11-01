setInterval(function() {
    fetch("../getTimeRemaining")
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        document.querySelector("#timeRemainingOfSession").innerHTML = data.timeRemaining
                    }
                )
            }
        }
    )
}, 1000);


