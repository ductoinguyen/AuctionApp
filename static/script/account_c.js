var mangNoiDungSanPham = {};

function contentSetRoom() {
    return '<div class="col-md-5 p-0" style="margin-left: 15px; margin-bottom: 15px; padding-left: 0; padding-right: 7.5px">' +
                '<input class="form-control" type="date">'+
            '</div>' +
            '<div class="col-md-5 p-0" style="padding: 0 7.5px;margin-left: 15px; margin-bottom: 15px">'+
                '<select class="form-control">'+
                    '<option value="-1">Chọn phiên</option>'+
                    '<option value="0">0</option>'+
                    '<option value="1">1</option>'+
                    '<option value="2">2</option>'+
                    '<option value="3">3</option>'+
                    '<option value="4">4</option>'+
                    '<option value="5">5</option>'+
                    '<option value="6">6</option>'+
                    '<option value="7">7</option>'+
                    '<option value="8">8</option>'+
                    '<option value="9">9</option>'+
                    '<option value="10">10</option>'+
                    '<option value="11">11</option>'+
                    '<option value="12">12</option>'+
                    '<option value="13">13</option>'+
                    '<option value="14">14</option>'+
                    '<option value="15">15</option>'+
                    '<option value="16">16</option>'+
                    '<option value="17">17</option>'+
                    '<option value="18">18</option>'+
                    '<option value="19">19</option>'+
                    '<option value="20">20</option>'+
                    '<option value="21">21</option>'+
                    '<option value="22">22</option>'+
                    '<option value="23">23</option>'+
                '</select>'+
            '</div>';
}

function contentHTMLRequest(tenSanPham, giaSanPham, loaiSanPham, anhSanPham, idSanPham, ngayTaoYeuCau) {
    return '<div class="row bg-light p-0" style="margin: 15px 0; border: 1px solid rgba(0, 0, 0, 0.15); border-radius: 0.25rem; box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.175);">'+
                '<div class="col-md-12">'+
                    '<div class="row">'+
                        '<div class="col-md-11 p-0"><h5 class="mb-0 pb-0" style="padding: 15px">'+ tenSanPham +'</h5></div>'+
                        '<div class="col-md-1 p-0" class="previewBtn" style="text-align: center; margin-top: 10px; cursor: pointer" onclick="hienThiThemThongTin(this)">'+
                            '<i class="fa fa-caret-down" style="width: 20px"></i>'+
                        '</div>'+
                    '</div>'+
                    '<div class="row">'+
                        '<div class="col-md-11 p-0"><h5 class="mb-0 pb-0" style="padding: 15px">ID: '+ idSanPham +'</h5></div>'+
                    '</div>'+
                    '<div class="row">'+
                        '<div class="col-md-11 p-0"><h5 class="mb-0 pb-0" style="padding: 15px">Ngày tạo yêu cầu: '+ ngayTaoYeuCau +'</h5></div>'+
                    '</div>'+
                    '<div class="row">'+
                        '<div class="col-md-5 p-0"><h5 class="mb-0 pb-0" style="padding: 15px; padding-right: 0;"> Giá khởi điểm: </h5></div>'+
                        '<div class="col-md-4 p-0"><h5 class="mb-0 pb-0" style="padding: 15px 0; padding-right: 15px;">'+ giaSanPham +'</h5></div>'+
                        '<div class="col-md-3 p-0"><h5 class="mb-0 pb-0" style="padding: 15px 0;">VNĐ</h5></div>'+
                    '</div>'+
                    '<div class="row">'+
                        '<div class="p-0"><h5 class="mb-0" style="padding: 15px">Loại:</h5></div>'+
                        '<div class="p-0"><h5 class="mb-0 pl-0" style="padding: 15px; width: 118px;">'+ loaiSanPham +'</h5></div>'+
                        '<div onclick="chapNhan(this)" style="padding: 7.5px; color: white;"><a class="btn btn-primary bg-success border-0">Chấp nhận</a></div>'+
                        '<div onclick="tuChoi(this)"style="padding: 7.5px; color: white;"><a class="btn btn-primary bg-danger border-0">Từ chối</a></div>'+
                    '</div>'+
                    '<div class="row style="padding: 15px">'+ contentSetRoom() + '</div>'+
                '</div>'+
                '<div class="col-md-12 divAnh" style="padding-bottom: 15px; display: none;">'+
                    '<img src="'+ anhSanPham +'" style="width: 100%; position: relative; border: 1px solid rgba(0, 0, 0, 0.15);">'+
                '</div>'+
            '</div>';
}

function chapNhan(elmt) {
    id_item = elmt.parentNode.parentNode.childNodes[1].childNodes[0].childNodes[0].innerHTML.substring(4);
    open_bid = elmt.parentNode.nextSibling.childNodes[0].childNodes[0].value;
    id_session = elmt.parentNode.nextSibling.childNodes[1].childNodes[0].value;
    // alert(open_bid + id_session)
    if (id_session < 0 || open_bid == "") {
        alert("Nhập đầy đủ thông tin phiên đấu giá!")
    } else {
        fetch("../acceptRequest", {
            method: "POST",
            credentials: "include",
            body: JSON.stringify({id_item: id_item, open_bid: open_bid, id_session: id_session}),
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
                            if (data.result == "ok") {
                                alert("Thành công!")
                                elmt.parentNode.parentNode.parentNode.remove()
                            } else {
                                alert("Hệ thống đang bận, vui lòng thử lại sau!")
                            }
                        }
                    )
                } else {
                    alert("Hệ thống đang bận, vui lòng thử lại sau!")
                }
            }
        )
    }

}

function tuChoi(elmt) {
    id_item = elmt.parentNode.parentNode.childNodes[1].childNodes[0].childNodes[0].innerHTML.substring(4);
    fetch("../refuseRequest/" + id_item)
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        if (data.result == "ok") {
                            alert("Thành công!")
                            elmt.parentNode.parentNode.parentNode.remove()
                        } else {
                            alert("Hệ thống đang bận, vui lòng thử lại sau!")
                        }
                    }
                )
            } else {
                alert("Hệ thống đang bận, vui lòng thử lại sau!")
            }
        }
    )
}

fetch("../getAllRequestFromC")
.then(
    resp => {
        if (resp.status == 200) {
            resp.json()
            .then(
                data => {
                    mangNoiDungSanPham = {}
                    for (var i = 0; i < data.length; i++) {
                        var item = data[i];
                        document.getElementById("cacYeuCau").innerHTML += contentHTMLRequest(item["name"], item["price_start"], item["category"], item["image"], item["id"], item["create_date"])
                        mangNoiDungSanPham["ID: " + item["id"]] = item["content"]
                    }
                }
            )
        }
    }
)

function hienThiThemThongTin(elmt) {
    icon = elmt.childNodes[0]
    if (icon.className == 'fa fa-caret-down') {
        icon.className = 'fa fa-caret-down open'
    } else {
        icon.className = 'fa fa-caret-down'
    }

    image = elmt.parentNode.parentNode.nextSibling
    $(image).slideToggle();
    $(image).hover(function() {
        id_item = elmt.parentNode.nextSibling.childNodes[0].childNodes[0].innerHTML
        document.getElementById("content-item").innerHTML = mangNoiDungSanPham[id_item]
        $("#content-item").slideToggle(100);
    });
}

function refeshRequest() {
    fetch("../getAllRequestFromC")
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        mangNoiDungSanPham = {}
                        for (var i = 0; i < data.length; i++) {
                            var item = data[i];
                            document.getElementById("cacYeuCau").innerHTML += contentHTMLRequest(item["name"], item["price_start"], item["category"], item["image"], item["id"], item["create_date"])
                            mangNoiDungSanPham["ID: " + item["id"]] = item["content"]
                        }
                    }
                )
            }
        }
    )
}

function xoaTaiKhoan() {
    username = document.getElementById("userNameXoa").value
    fetch("../xoaTaiKhoan/" + username)
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        if (data.result == "ok") {
                            alert("Thành công!")
                            document.getElementById("userNameXoa").value = ""
                        } else {
                            alert("Hệ thống đang bận, vui lòng thử lại sau!")
                        }
                    }
                )
            } else {
                alert("Hệ thống đang bận, vui lòng thử lại sau!")
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

function renderContentFilter(item) {
    var content = '<div class="row mb-2" style="padding: 15px; border: 1px solid rgba(0, 0, 0, 0.15); border-radius: 0.25rem; box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.175); margin: 0; background-color: #ffffff;">'+
                '<div class="col-md-12">'+
                    '<div class="row">'+
                        '<div class="col-md-7 pl-0">'+
                            '<div class="row">'+
                                '<div class="col-md-12">'+'<h6 id="searchName">'+ item.name + '</h6>'+'</div>'+
                            '</div>'+
                            '<div class="row">'+
                                '<div class="col-md-2">' + '<h6> ID: </h6>'+ '</div>'+
                                '<div class="col-md-10">'+ '<h6>' + item.id_item + '</h6>'+ '</div>'+
                            '</div>'+
                            '<div class="row">'+
                                '<div class="col-md-3 pr-0">'+ '<h6> Giá mở: </h6>'+ '</div>'+ 
                                '<div class="col-md-4 px-0 text-right">'+'<h6>'+ formatMoney(item.price_start) +' </h6>'+ '</div>'+
                                '<div class="col-md-5"><h6> VNĐ </h6></div>'+
                            '</div>'+
                            '<div class="row">' + 
                                '<div class="col-md-4 pr-0">'+'<h6> Người bán: </h6>'+'</div>'+
                                '<div class="col-md-8"> <h6> ' + item.name_auction + '</h6> </div>'+
                            '</div>'+
                            '<div class="row">'+
                                '<div class="col-md-12"><h6><b><em> '+ item.status +' </em></b></h6></div>'+
                            '</div>';
                            if (item.status == 'Đã đấu giá') {
                                content += '<div class="row">'+
                                                '<div class="col-md-12"><h6><b><em>Người mua: '+ item.name_bidder +' </em></b></h6></div>'+
                                            '</div>' +
                                            '<div class="row">'+
                                                '<div class="col-md-12"><h6><b><em>Giá mua: '+ formatMoney(item.price_max) +' </em></b></h6></div>'+
                                            '</div>';
                            } else if (item.status == 'Đang đấu giá') {
                                content += '<div class="row">'+
                                                '<div class="col-md-12"><h6><b><em>Người đang đấu giá cao nhất: '+ item.name_bidder +' </em></b></h6></div>'+
                                            '</div>' +
                                            '<div class="row">'+
                                                '<div class="col-md-12"><h6><b><em>Giá đấu: '+ formatMoney(item.price_max) +' </em></b></h6></div>'+
                                            '</div>';
                            }
            content += '</div>'+
                        '<div class="col-md-5 p-0">'+
                            '<img id="searchItemImg" style="width: 100%; border: 1px solid rgba(0, 0, 0, 0.15);" src="' + item.image + '">'+
                        '</div>'+
                    '</div>'+
                '</div>'+
            '</div>';
    return content;
}

function filterItem(open_bid, index_session, category) {
    fetch("../filterItem", {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({open_bid: open_bid, index_session: index_session, category: category}),
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
                        var contentHTML = ""
                        console.log(data)
                        for (var i = 0; i < data.length; i++) {
                            contentHTML += renderContentFilter(data[i])
                        }
                        document.getElementById("noiDungLoc").innerHTML = contentHTML;
                    }
                )
            } else {
                // alert("Hệ thống đang bận, vui lòng thử lại sau!")
            }
        }
    )
}

var filterDate = document.getElementById("filterDate");
var filterHour = document.getElementById("filterHour");
var filterCategory = document.getElementById("filterCategory");

filterDate.onchange = function () {
    if (filterHour.value != "" && filterCategory.value != "") {
        filterItem(filterDate.value, filterHour.value, filterCategory.value)  
    }
}

filterHour.onchange = function () {
    if (filterDate.value != "" && filterCategory.value != "") {
        filterItem(filterDate.value, filterHour.value, filterCategory.value)  
    }
}
filterCategory.onchange = function () {
    if (filterHour.value != "" && filterDate.value != "") {
        filterItem(filterDate.value, filterHour.value, filterCategory.value)  
    }
}