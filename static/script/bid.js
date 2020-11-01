var loaiphong = location.pathname.split("/")[2]
var tenCacPhong = {
    "trangsuc": "Phòng Trang sức",
    "doco": "Phòng Đồ cổ",
    "hoihoa": "Phòng Hội họa",
    "thoitrang": "Phòng Thời trang",
    "doluuniem": "Phòng Đồ lưu niệm"
}
document.querySelector("#tenPhong").innerHTML = tenCacPhong[loaiphong]
function loadLaiNoiDung() {
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
                            document.querySelector("#giaKhoiDiem").innerHTML = data.price_start
                            document.querySelector("#giaLonNhat").innerHTML = data.price_max
                            alert("OK")
                            var id_auctioneer = data.id_auctioneer
                        } else {
                            alert("Loi")
                        }
                        
                    }
                )
            }
        }
    )
}
loadLaiNoiDung()