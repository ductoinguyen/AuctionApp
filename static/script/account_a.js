function sendRequest() {
    name = document.getElementById("reqName").value;
    content = document.getElementById("reqContent").value;
    image = document.getElementById("reqImage").value;
    category = document.getElementById("reqCategory").value;
    fetch("../getIdAuctioneer")
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        id_auctioneer = data.id_auctioneer;
                    }
                )
            }
        }
    )
    price_start = document.getElementById("reqOpenPrice").value;
    fetch("../createRequestFromA", {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({name: name, content: content, image: image, category: category, id_auctioneer: id_auctioneer, price_start: price_start, price_max: price_start,}),
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

fetch("../getIdAuctioneer")
.then(
    resp => {
        if (resp.status == 200) {
            resp.json()
            .then(
                data => {
                    document.getElementById("auctioneerBalance").innerHTML += formatMoney(data.accountBalance) + ' VNĐ';
                }
            )
        }
    }
)

fetch("../getAllRequestFromA")
.then(
    resp => {
        if (resp.status == 200) {
            resp.json()
            .then (
                data => {
                    for (var i = 0; i < data.length; i++) {
                        var contentHTML = ""
                        var item = data[i]
                        contentHTML +=
                        '<div class="row bg-light p-0" style="margin: 15px 0; border: 1px solid rgba(0, 0, 0, 0.15); border-radius: 0.25rem; box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.175);">'+
                            '<div class="col-md-12">'+
                                '<div class="row">'+
                                    '<div class="col-md-12 p-0">'+
                                        '<h5 class="mb-0 pb-0" style="padding: 15px">'+ item["name"] +'</h5>'+
                                    '</div>'+
                                '</div>'+
                                '<div class="row">'+
                                    '<div class="col-md-12 p-0"><h5 class="mb-0 pb-0" style="padding: 15px">Ngày tạo yêu cầu: '+ item["create_date"] +'</h5></div>'+
                                '</div>'



                        if (item["status"] == "ready to auction") {
                            contentHTML +=
                                '<div class="row">'+
                                    '<div class="col-md-4 p-0">'+
                                        '<h5 class="mb-0 pb-0 pr-0" style="padding: 15px" > Ngày đấu giá: </h5>'+
                                    '</div>'+
                                    '<div class="col-md-4 p-0 text-right">'+
                                        '<h5 class="mb-0 pb-0" style="padding: 15px;">'+ item["open_bid"] +'</h5>'+
                                    '</div>'+
                                '</div>'+
                                '<div class="row">'+
                                    '<div class="col-md-4 p-0">'+
                                        '<h5 class="mb-0 pb-0" style="padding: 15px; padding-right: 0;"> Giá khởi điểm: </h5>'+
                                    '</div>'+
                                    '<div class="col-md-4 p-0">'+
                                        '<h5 class="mb-0 pb-0 text-right" style="padding: 15px 0; padding-right: 15px;">'+ item["price_start"] +'</h5>'+
                                    '</div>'+
                                    '<div class="col-md-4 p-0">'+
                                        '<h5 class="mb-0 pb-0" style="padding: 15px 0;">VNĐ</h5>'+
                                    '</div>'+
                                '</div>'+
                                '<div class="row">'+
                                    '<div class="col-md-2 p-0">'+
                                        '<h5 class="mb-0" style="padding: 15px">Loại:</h5>'+
                                    '</div>'+
                                    '<div class="col-md-6 p-0">'+
                                        '<h5 class="mb-0" style="padding: 15px">'+ item["category"] +'</h5>'+
                                    '</div>'+
                                    '<div class="col-md-4 p-0">'+
                                        '<h5 class="mb-0 text-success text-right" style="font-weight: 500; padding: 15px;"><em>Thành công</em></h5>'+
                                    '</div>'+
                                '</div>'
                        } else
                        if (item["status"] == "fail") {
                            contentHTML +=
                                '<div class="row">'+
                                    '<div class="col-md-4 p-0">'+
                                        '<h5 class="mb-0 pb-0" style="padding: 15px; padding-right: 0;"> Giá khởi điểm: </h5>'+
                                    '</div>'+
                                    '<div class="col-md-4 p-0">'+
                                        '<h5 class="mb-0 pb-0 text-right" style="padding: 15px 0; padding-right: 15px;">'+ item["price_start"] +'</h5>'+
                                    '</div>'+
                                    '<div class="col-md-4 p-0">'+
                                        '<h5 class="mb-0 pb-0" style="padding: 15px 0;">VNĐ</h5>'+
                                    '</div>'+
                                '</div>'+
                                '<div class="row">'+
                                    '<div class="col-md-2 p-0">'+
                                        '<h5 class="mb-0" style="padding: 15px">Loại:</h5>'+
                                    '</div>'+
                                    '<div class="col-md-6 p-0">'+
                                        '<h5 class="mb-0" style="padding: 15px">'+ item["category"] +'</h5>'+
                                    '</div>'+
                                    '<div class="col-md-4 p-0">'+
                                        '<h5 class="mb-0 text-danger text-right" style="font-weight: 500; padding: 15px;"><em>Thất bại</em></h5>'+
                                    '</div>'+
                                '</div>'
                        } else
                        if (item["status"] == "handling") {
                            contentHTML +=
                                '<div class="row">'+
                                    '<div class="col-md-4 p-0">'+
                                        '<h5 class="mb-0 pb-0" style="padding: 15px; padding-right: 0;"> Giá khởi điểm: </h5>'+
                                    '</div>'+
                                    '<div class="col-md-4 p-0">'+
                                        '<h5 class="mb-0 pb-0 text-right" style="padding: 15px 0; padding-right: 15px;">'+ item["price_start"] +'</h5>'+
                                    '</div>'+
                                    '<div class="col-md-4 p-0">'+
                                        '<h5 class="mb-0 pb-0" style="padding: 15px 0;">VNĐ</h5>'+
                                    '</div>'+
                                '</div>'+
                                '<div class="row">'+
                                    '<div class="col-md-2 p-0">'+
                                        '<h5 class="mb-0" style="padding: 15px">Loại:</h5>'+
                                    '</div>'+
                                    '<div class="col-md-6 p-0">'+
                                        '<h5 class="mb-0" style="padding: 15px">'+ item["category"] +'</h5>'+
                                    '</div>'+
                                    '<div class="col-md-4 p-0">'+
                                        '<h5 class="mb-0 text-right" style="font-weight: 500; padding: 15px;"><em>Chờ duyệt</em></h5>'+
                                    '</div>'+
                                '</div>'
                        }
                                
                        contentHTML +=
                            '</div>'+
                        '</div>'
                        document.getElementById("requestList").innerHTML += contentHTML;
                    }
                }
            )
        }
    }
)