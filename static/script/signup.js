document.getElementById("form11").onblur = function() {
    fetch("../checkAccount/" + document.getElementById("form11").value)
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        if (data.result == -1) {
                            alert("Username đã tồn tại!")
                            // document.getElementById("form11").focus()
                        }
                    }
                )
            }
        }
    )
}

function submitSignUp() {
    username = document.querySelector("#form11").value 
    password = document.querySelector("#form12").value 
    nameAccount = document.querySelector("#form36").value
    birthday = document.querySelector("#form37").value
    address = document.querySelector("#form38").value
    phoneNumber = document.querySelector("#form40").value

    fetch("../checkAccount/" + document.getElementById("form11").value)
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        if (data.result == -1) {
                            alert("Username đã tồn tại!")
                            // document.getElementById("form11").focus()
                        } else {
                            if (username == "" || password == "" || nameAccount == "" || birthday == "" || address == "" || phoneNumber == "") {
                                alert("Cần nhập đầy đủ thông tin")
                            } else {
                                fetch("../submitSignup", {
                                    method: "POST",
                                    credentials: "include",
                                    body: JSON.stringify({username: username, password: password, nameAccount: nameAccount, birthday: birthday, address: address, phoneNumber: phoneNumber}),
                                    cache: "no-cache",
                                    headers: new Headers({
                                        "content-type": "application/json"
                                    })      
                                })
                                .then(
                                    resp => {
                                        if (resp.status == 200) {
                                            resp.json()
                                            .then(
                                                data => {
                                                    if (data.result == "Thành công") {
                                                        alert("Thành công!")
                                                        location.href = '/';
                                                    } else {
                                                        alert("Vui lòng kiểm tra lại các trường thông tin!")
                                                    }
                            
                                                }
                                            )
                                        }
                                    }
                                )
                            }
                        }
                    }
                )
            }
        }
    )
}