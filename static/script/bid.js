var loaiphong = location.pathname.split("/")[2]
var id_item = ""
var tenCacPhong = {
    "trangsuc": "Phòng Trang sức",
    "doco": "Phòng Đồ cổ",
    "hoihoa": "Phòng Hội họa",
    "thoitrang": "Phòng Thời trang",
    "doluuniem": "Phòng Đồ lưu niệm"
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

document.querySelector("#tenPhong").innerHTML = tenCacPhong[loaiphong]
setInterval(function() {
    fetch("../san-pham-chinh/" + loaiphong)
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        if (data.status == "SUC") {
                            document.querySelector("#tenSanPham").innerHTML = data.title
                            document.querySelector("#noiDungSanPham").innerHTML = data.description
                            document.querySelector("#anhSanPham").src = data.image
                            document.querySelector("#giaKhoiDiem").innerHTML = formatMoney(data.price_start)
                            id_item = data.id_item
                            // document.querySelector("#giaLonNhat").innerHTML = formatMoney(data.price_max)
                            // alert("OK")
                            var id_auctioneer = data.id_auctioneer
                        } else {
                            location.href = '../cac-phong-dau-gia'
                        }                        
                    }
                )
            }
        }
    )
}, 3000);

setInterval(function() {
    fetch("../pricemax-time/" + loaiphong)
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        if (data.status == "SUC") {
                            document.querySelector("#timeRemaining").innerHTML = data.timeRemaining
                            document.querySelector("#giaLonNhat").innerHTML = formatMoney(data.price_max)
                            if (data.flagTop1Bidder == 1) {
                                document.querySelector("#thongBao").style.display = "block"
                            } else {
                                document.querySelector("#thongBao").style.display = "none"
                            }
                            
                            // alert(data.timeRemaining + " " + data.price_max)
                        } else {
                            // alert("Loi")
                        }
                        
                    }
                )
            }
        }
    )
}, 1000);

function eventTraGia() {
    price = document.querySelector("input").value
    fetch("../tra-gia", {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({price: price, id_item: id_item}),
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
                        alert(data.result)
                    }
                )
            }
        }
    )
}