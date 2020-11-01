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

setInterval(function() {
    fetch("../getItemInRoom/thoitrang")
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        if (data[data.length - 1].status == "NULL") {
                            document.querySelector("#mienThoiTrang").innerHTML = "<div style='margin-left:10px'>Các sản phẩm đã đấu giá hết, vui lòng đợi phiên đấu giá sau!</div>"
                            document.querySelector("#buttonThoiTrang").style.display = "none";
                        } else {
                            document.querySelector("#buttonThoiTrang").style.display = "block";
                            var contentHTML = ""
                            for (let i = 0; i < data.length - 1; i++) {
                                contentHTML +=
                                    '<a href="/chi-tiet-san-pham/' + data[i].id_item + '"><div class="col-md-4">'
                                        + '<img src="'+ data[i].image + '" style="width: 330px; border-radius: 10px; height: 330px;">'
                                    + '</div></a>'
                            }
                            document.querySelector("#mienThoiTrang").innerHTML = contentHTML;
                        }
                    }
                )
            }
        }
    )
}, 1000);

setInterval(function() {
    fetch("../getItemInRoom/hoihoa")
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        if (data[data.length - 1].status == "NULL") {
                            document.querySelector("#mienHoiHoa").innerHTML = "<div style='margin-left:10px'>Các sản phẩm đã đấu giá hết, vui lòng đợi phiên đấu giá sau!</div>"
                            document.querySelector("#buttonHoiHoa").style.display = "none";
                        } else {
                            var contentHTML = ""
                            document.querySelector("#buttonHoiHoa").style.display = "block";
                            for (let i = 0; i < data.length - 1; i++) {
                                contentHTML +=
                                    '<a href="/chi-tiet-san-pham/' + data[i].id_item + '"><div class="col-md-4">'
                                        + '<img src="'+ data[i].image + '" style="width: 330px; border-radius: 10px; height: 330px;">'
                                    + '</div></a>'
                            }
                            document.querySelector("#mienHoiHoa").innerHTML = contentHTML;
                        }
                    }
                )
            }
        }
    )
}, 1000);

setInterval(function() {
    fetch("../getItemInRoom/trangsuc")
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        if (data[data.length - 1].status == "NULL") {
                            document.querySelector("#mienTrangSuc").innerHTML = "<div style='margin-left:10px'>Các sản phẩm đã đấu giá hết, vui lòng đợi phiên đấu giá sau!</div>"
                            document.querySelector("#buttonTrangSuc").style.display = "none";
                        } else {
                            var contentHTML = ""
                            document.querySelector("#buttonTrangSuc").style.display = "block";
                            for (let i = 0; i < data.length - 1; i++) {
                                contentHTML +=
                                    '<a href="/chi-tiet-san-pham/' + data[i].id_item + '"><div class="col-md-4">'
                                        + '<img src="'+ data[i].image + '" style="width: 330px; border-radius: 10px; height: 330px;">'
                                    + '</div></a>'
                            }
                            document.querySelector("#mienTrangSuc").innerHTML = contentHTML;
                        }
                    }
                )
            }
        }
    )
}, 1000);

setInterval(function() {
    fetch("../getItemInRoom/doluuniem")
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        if (data[data.length - 1].status == "NULL") {
                            document.querySelector("#mienDoLuuNiem").innerHTML = "<div style='margin-left:10px'>Các sản phẩm đã đấu giá hết, vui lòng đợi phiên đấu giá sau!</div>"
                            document.querySelector("#buttonDoLuuNiem").style.display = "none";
                        } else {
                            var contentHTML = ""
                            document.querySelector("#buttonDoLuuNiem").style.display = "block";
                            for (let i = 0; i < data.length - 1; i++) {
                                contentHTML +=
                                    '<a href="/chi-tiet-san-pham/' + data[i].id_item + '"><div class="col-md-4">'
                                        + '<img src="'+ data[i].image + '" style="width: 330px; border-radius: 10px; height: 330px;">'
                                    + '</div></a>'
                            }
                            document.querySelector("#mienDoLuuNiem").innerHTML = contentHTML;
                        }
                    }
                )
            }
        }
    )
}, 1000);

setInterval(function() {
    fetch("../getItemInRoom/doco")
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        if (data[data.length - 1].status == "NULL") {
                            document.querySelector("#mienDoCo").innerHTML = "<div style='margin-left:10px'>Các sản phẩm đã đấu giá hết, vui lòng đợi phiên đấu giá sau!</div>"
                            document.querySelector("#buttonDoCo").style.display = "none";
                        } else {
                            var contentHTML = ""
                            document.querySelector("#buttonDoCo").style.display = "block";
                            for (let i = 0; i < data.length - 1; i++) {
                                contentHTML +=
                                    '<a href="/chi-tiet-san-pham/' + data[i].id_item + '"><div class="col-md-4">'
                                        + '<img src="'+ data[i].image + '" style="width: 330px; border-radius: 10px; height: 330px;">'
                                    + '</div></a>'
                            }
                            document.querySelector("#mienDoCo").innerHTML = contentHTML;
                        }
                    }
                )
            }
        }
    )
}, 1000);