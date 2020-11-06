function formatMoney(amount, decimalCount = 0, decimal = ".", thousands = ",") {
    try {
        decimalCount = Math.abs(decimalCount);
        decimalCount = isNaN(decimalCount) ? 2 : decimalCount;
    
        const negativeSign = amount < 0 ? "-" : "";
    
        let i = parseInt(amount = Math.abs(Number(amount) || 0).toFixed(decimalCount)).toString();
        let j = (i.length > 3) ? i.length % 3 : 0;
    
        return negativeSign + (j ? i.substr(0, j) + thousands : '') + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + thousands) + (decimalCount ? decimal + Math.abs(amount - i).toFixed(decimalCount).slice(2) : "");
    } catch (e) {
        console.log(e)
    }
};

fetch("../getInfoBidder")
.then(
    resp => {
        if (resp.status == 200) {
            resp.json()
            .then(
                data => {
                    document.getElementById("tenTaiKhoan").value = data.name;
                    document.getElementById("address").value = data.address;
                    document.getElementById("birthDay").value = data.birthday;
                    // alert(data.birthday)
                    document.getElementById("soDuTaiKhoan").innerHTML = formatMoney(data.accountBalance);
                    document.getElementById("phone").value = data.phoneNumber;
                }
            )
        }
    }
)

function updateInformation() {
    nameAccount = document.getElementById("tenTaiKhoan").value;
    address = document.getElementById("address").value;
    birthday = document.getElementById("birthDay").value;
    phoneNumber = document.getElementById("phone").value;
    fetch("../setInfoBidder", {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({nameAccount: nameAccount, address: address, birthday: birthday, phoneNumber: phoneNumber}),
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
                        // alert(data.result)
                        if (data.result == "success") {
                            alert("Thành công!")
                        } else {
                            // alert(data.result)
                        }

                    }
                )
            }
        }
    )
}