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
                    // alert(data.accountBalance)
                    document.getElementById("account-balance").innerHTML = formatMoney(data.accountBalance) + " VND";
                }
            )
        }
    }
)

fetch("../getAllHistoryAuction")
.then(
    resp => {
        if (resp.status == 200) {
            resp.json()
            .then(
                data => {
                    if (data.length == 0) {
                        alert("Chưa có lịch sử đấu giá!")
                        location.href = '/';
                    }
                    var thatbai = '<h4 class="px-2" style="font-weight: 700; font-size: 30px; color: red;"> THẤT BẠI </h4>'
                    var thanhcong = '<h4 class="px-2 text-success" style="font-weight: 700; font-size: 30px;"> THÀNH CÔNG </h4>'
                    var dangdienra = '<h4 class="px-2" style="font-weight: 700; font-size: 30px;"> ĐANG DIỄN RA </h4>'
                    var contentHTML = "", trangthai = ""
                    for (var i = 0; i < data.length; i++) {
                        item = data[i];
                        if (item.status == "Thành công") {
                            trangthai = thanhcong;
                        } else if (item.status == "Thất bại") {
                            trangthai = thatbai;
                        } else {
                            trangthai = dangdienra;
                        }
                        trangthai =
                        contentHTML += 
                        '<div class="each-item container my-3" style="border-radius: 7px; background-color: white; box-shadow: 2px 2px 10px grey;">'+
                            '<div class="row">'+
                            '<div class="col-md-8 details py-2">'+
                                '<div class="row item-name my-2">'+
                                '<div class="col-md-4">'+
                                    '<h4 style="font-size: 30px;" class="border-bottom pl-2"><b> Tên SP: </b></h4>'+
                                '</div>'+
                                '<div class="col-md-8">'+
                                    '<h4 style="font-size: 30px;" class="border-bottom"><b>' + item.item_name + '</b></h4>'+
                                '</div>'+
                                '</div>'+
                                '<div class="row open-bid my-2">'+
                                '<div class="col-md-4">'+
                                    '<h4 style="font-size: 30px;" class="pl-2 border-bottom"><b> Giá gốc: </b></h4>'+
                                '</div>'+
                                '<div class="col-md-4 pr-0">'+
                                    '<h4 style="font-size: 30px;" class="border-bottom">'+ formatMoney(item.price_start) + '</h4>'+
                                '</div>'+
                                '<div class="col-md-4 pl-0">'+
                                    '<h4 style="font-size: 30px;" class="border-bottom"> VNĐ </h4>'+
                                '</div>'+
                                '</div>'+
                                '<div class="row status my-2">'+
                                '<div class="col-md-4" style="">'+
                                    '<h4 style="font-size: 30px;" class="pl-2 border-bottom"><b> Trạng thái: </b></h4>'+
                                '</div>'+
                                '<div class="col-md-8 pl-0" style="">'+trangthai+'</div>'+
                                '</div>'+
                                '<div class="row paid my-2">'+
                                '<div class="col-md-4">'+
                                    '<h4 style="font-size: 30px;" class="pl-2 border-bottom"><b> Giá trả: </b></h4>'+
                                '</div>'+
                                '<div class="col-md-4 pr-0">'+
                                    '<h4 style="font-size: 30px;" class="border-bottom">'+ formatMoney(item.price) +'</h4>'+
                                '</div>'+
                                '<div class="col-md-4 pl-0">'+
                                    '<h4 style="font-size: 30px;" class="border-bottom"> VNĐ </h4>'+
                                '</div>'+
                                '</div>'+
                                '<div class="row date">'+
                                '<div class="col-md-4">'+
                                    '<h4 style="font-size: 30px;" class="pl-2 border-bottom">'+
                                    '<b>Ngày đấu giá:</b>'+
                                    '</h4>'+
                                '</div>'+
                                '<div class="col-md-8" id="bid-date">'+
                                    '<h4 style="font-size: 30px;" class="border-bottom">'+ item.open_bid +'</h4>'+
                                '</div>'+
                                '</div>'+
                            '</div>'+
                            '<div class="col-md-4 picture" style="margin: 10px auto">'+
                                '<img src="'+ item.image+'" style="width: 330px;border-radius: 10px;height: 330px;">'+
                            '</div>'+
                            '</div>'+
                        '</div>';
                    }
                    document.getElementById("contentHistory").innerHTML = contentHTML;
                }
            )
        } else {
            alert("Hệ thống đang bận, vui lòng thử lại sau!")
            location.href = '/';
        }
    }
)