//var loaiphong = location.pathname.split("/")[2]
var id_item = location.pathname.split("/")[2]
/*var tenCacPhong = {
    "trangsuc": "Phòng Trang sức",
    "doco": "Phòng Đồ cổ",
    "hoihoa": "Phòng Hội họa",
    "thoitrang": "Phòng Thời trang",
    "doluuniem": "Phòng Đồ lưu niệm"
}*/

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

//document.querySelector("#tenPhong").innerHTML = tenCacPhong[loaiphong]
fetch("../thong-tin-san-pham/" + id_item)
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
                        // document.querySelector("#giaLonNhat").innerHTML = formatMoney(data.price_max)
                        // alert("OK")
                        var id_auctioneer = data.id_auctioneer
                        fetch("../thong-tin-ben-a/" + id_auctioneer)
                        .then(
                            resp => {
                                if (resp.status == 200) {
                                    resp.json()
                                    .then(
                                        data => {
                                            if (data.status == "SUC") {
                                                document.querySelector("#tenBenA").innerHTML = data.name
                                                document.querySelector("#soDienThoai").innerHTML = data.phoneNumber
                                                document.querySelector("#diaChiBenA").innerHTML = data.address                                                    
                                            } else {
                                                
                                            }                        
                                        }
                                    )
                                }
                            }
                        )
                    } else {
                        location.href = '../cac-phong-dau-gia'
                    }                        
                }
            )
        }
    }
)
