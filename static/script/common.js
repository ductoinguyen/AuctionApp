fetch("../getNameAccount")
.then(
    resp => {
        if (resp.status == 200) {
            resp.json()
            .then(
                data => {
                    document.querySelector("#nameAccount").innerHTML = data.name_account
                }
            )
        }
    }
)
