import pymongo
from pymongo import MongoClient

import random

myclient = MongoClient("mongodb+srv://hequantri:hequantri@cluster0.q0gxn.gcp.mongodb.net/auctionDB?retryWrites=true&w=majority")
db = myclient["auctionDB"]
    
def createUsername(i):
    return "testauctioneer" + str(i)
    
def createPassword():
    return 8413693891228823164

def randomHo():
    arr = ['Nguyễn', 'Hoàng', 'Vũ', 'Lê', 'Trần', 'Đào', 'Đàm', 'Phạm', 'Tạ', 
           'Vương', 'Bá', 'Nguyễn', 'Trần',	'Lê', 'Phạm',	'Hoàng', 'Huỳnh', 
           'Phan', 'Vũ', 'Võ', 'Đặng','Bùi','Đỗ', 'Hồ', 'Ngô', 'Dương', 'Lý']
    return arr[random.randint(0, len(arr) - 1)]

def randomTenDem(gioiTinh):
    if gioiTinh == 0:
        arr = ['Văn', 'Thành', 'Đức', 'Anh', 'Quốc', 'Tiến', 'Hải', 'Minh',
               'Việt', 'Toàn']

    elif gioiTinh == 1:
        arr = ['Thị', 'Phương', 'Huyền', 'Anh', 'Hồng', 'Thu', 'Ngọc', 'Quỳnh',
               'Mỹ', 'Thùy']

    return arr[random.randint(0,len(arr)-1)]

def randomTen(gioiTinh):
    if (gioiTinh == 0):
        # nam
        arr = ['Hoàng', 'Phong', 'Long', 'Hải', 'Trung', 'Duy', 'Tuấn', 'Anh', 
               'Đức', 'Phú', 'Quyết', 'Việt', 'Mạnh', 'Hải', 'Tuệ', 'Sáng', 
               'Nam', 'Minh', 'Sỹ', 'Toàn']
        return arr[random.randint(0, len(arr) - 1)]
    else:
        # nu
        arr = ['Lan', 'Nguyệt', 'My', 'Hà', 'Hương', 'Thúy', 'Thùy', 'Anh',
               'Trâm', 'Cúc', 'Thủy', 'Dương', 'Liễu', 'Hiền', 'Nga', 'Lụa',
               'Ngọc', 'Hường', 'Huế', 'Oanh', 'Ly']
        return arr[random.randint(0, len(arr) - 1)]

def createName():
    gioiTinh = 1 if random.random() > 0.5 else 0
    # 0: nam, 1: nu
    return randomHo() + " " + randomTenDem(gioiTinh) + " " + randomTen(gioiTinh)

# print(createName())

def randomPhoneNumber():
    return '0' + str(random.randint(6, 9)) + str(random.randint(2, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

# print(randomPhoneNumber())

def randomBirthday():
    namSinh = str(random.randint(1960, 1995))
    thangSinh = str(random.randint(1, 12))
    if (len(thangSinh) == 1):
        thangSinh = '0' + thangSinh
    ngaySinh = str(random.randint(1, 28))
    if (len(ngaySinh) == 1):
        ngaySinh = '0' + ngaySinh
    return ngaySinh + '-' + thangSinh + '-' + namSinh

def randomCreateDate():
    namSinh = str(random.randint(2018, 2020))
    thangSinh = str(random.randint(1, 12))
    if (len(thangSinh) == 1):
        thangSinh = '0' + thangSinh
    ngaySinh = str(random.randint(1, 28))
    if (len(ngaySinh) == 1):
        ngaySinh = '0' + ngaySinh
    return ngaySinh + '-' + thangSinh + '-' + namSinh
    
def randomRecentDay():
    namSinh = str(2020)
    thangSinh = str(random.randint(1, 12))
    if (len(thangSinh) == 1):
        thangSinh = '0' + thangSinh
    ngaySinh = str(random.randint(1, 28))
    if (len(ngaySinh) == 1):
        ngaySinh = '0' + ngaySinh
    return ngaySinh + '-' + thangSinh + '-' + namSinh

# print(randomBirthday())
# print(randomCreateDate())
# print(randomRecentDay())


address = db.address

def randomDiaChi():
    cityID = random.randint(1, 63)
    result = address.find({"id": str(cityID)})
    cityName = ""
    for city in result:
        cityName = city["name"]
        districtID = random.randint(0, len(city["districts"]) - 1)
        districtName = city["districts"][districtID]["name"]

        streetName = ""
        wardName = ""
        if len(city["districts"][districtID]["projects"]) > 0:
            streetID = random.randint(0, len(city["districts"][districtID]["projects"]) - 1)
            streetName = city["districts"][districtID]["projects"][streetID]["name"]
            return streetName + ', ' + districtName + ', ' + cityName
        else:
            wardID = random.randint(0, len(city["districts"][districtID]["wards"]) - 1)
            wardName = city["districts"][districtID]["wards"][wardID]["name"]
            return wardName + ', ' + districtName + ', ' + cityName

# print(randomDiaChi())

def randomBalance():
    return round(random.randint(500000000, 10000000000) + random.randint(0, 90000000)/90000000, 3)

# print(randomBalance())

def itemContent():
    category = createCategory()
    if category == 'Thời trang':
        links = [
            "https://s3-ap-southeast-1.amazonaws.com/images.spiderum.com/sp-images/b563d0f0bafd11e8a642376e30d5ddea.jpg",
            "https://s3-ap-southeast-1.amazonaws.com/images.spiderum.com/sp-images/be6e9310bafd11e886db39a9c6aec10a.jpg",
            "https://i.pinimg.com/originals/71/84/5f/71845f32b0494de5093b2d5254c3fe14.jpg",
            "https://snkrvn.com/wp-content/uploads/2015/12/edo.jpg",
            "https://hips.hearstapps.com/hbz.h-cdn.co/assets/15/35/hbz-michael-jackson-1993-gettyimages-88796056.jpg",
            "https://ae01.alicdn.com/kf/HTB1In_OSpXXXXayaXXXq6xXFXXXp/Rare-PUNK-Formal-dress-Classic-England-Style-MJ-MICHAEL-JACKSON-Costume-Military-Jacket-Belt-Hat-For.jpg",
            "http://fashionnet.vn/public/uploads/images/81509229_10156336584547924_3002219596313788416_o.jpg",
            "http://fashionnet.vn/public/uploads/images/80504137_10156336626522924_8818530953564520448_o.jpg",
            "https://i1-giaitri.vnecdn.net/2018/01/10/le-thanh-hoa-1515572750.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=Y3x2NQyZaLMLDiIbah-spg",
            "https://i1-giaitri.vnecdn.net/2018/01/10/hoang-hai-1515568980.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=-FVRtlrfX1mbp4vujq7KZw",
            "https://i1-giaitri.vnecdn.net/2018/01/10/cong-tri-3-1515572749.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=XfeGB3-I1uLI_9St8IHYqw",
            "https://i1-giaitri.vnecdn.net/2018/01/10/cong-tri-2-1515572749.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=feEqJfbx2WYdd3mvxc0N5g",
            "https://i1-giaitri.vnecdn.net/2018/01/10/life-in-color-do-manh-cuong-1515578463.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=jQqXt_wm76MWEmqJsp1s1Q",
            "https://i1-giaitri.vnecdn.net/2018/01/10/chung-thanh-phong-1515572748.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=t5Fr9CAGUBTZ1iuh98H5SQ",
            "https://i1-giaitri.vnecdn.net/2018/01/10/3-1509073985-680x0-1515572751.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=HQZoR2SYeEH3tQ7v83yu5A",
            "https://i.doanhnhansaigon.vn/2014/08/08/8-large-1508390751.jpg",
            "https://ae01.alicdn.com/kf/HTB1X64QjmcqBKNjSZFgq6x_kXXaC.jpg_q50.jpg",
            "https://bizweb.dktcdn.net/100/356/785/articles/trang-phuc-ai-cap-009.jpg?v=1594599835823",
            "https://cafebiz.cafebizcdn.vn/thumb_w/600/2018/12/27/photo-1-154581447670622118320-154589765893056633362-crop-15458978335481123839352.png",
            "https://ae01.alicdn.com/kf/H2d59cc7b22674a8ea3eadf6ccc49c9baF/Rococo-Baroque-Marie-Antoinette-B-ng-o-18th-Th-K-Th-i-Ph-c-H-ng.jpg_q50.jpg",
            "https://ae01.alicdn.com/kf/HTB1lbTlmY1YBuNjSszhq6AUsFXaO.jpg_q50.jpg"
        ]
        describe = "Hẳn với những người yêu thời trang, fashion show là một sự kiện không thể bỏ lỡ vì nó không chỉ là một đường băng với các người mẫu mặc những bộ đồ ấn tượng đi qua đi lại mà nó còn đọng lại trong lòng khán giả như một buổi trình diễn nghệ thuật, là sự giao thoa giữa mỹ thuật, âm nhạc, ánh sáng và bài trí sân khấu. Dĩ nhiên, fashion show được sinh ra không phải chỉ để dành cho thưởng lãm bởi chi phí tổ chức một fashion show là rất lớn. Fashion show có một nhiệm vụ quan trọng trong việc quảng bá sản phẩm của các nhà thiết kế và quan trọng hơn nữa là để khẳng định danh tiếng của hãng."

    if category == 'Hội họa':
        links= [
            "https://media.baltictimes.com/media/photos/146160_1766082905d9dd3947a871_big.jpg",
            "https://i.ytimg.com/vi/TTMWZaTYSc4/maxresdefault.jpg",
            "https://www.europeanceo.com/wp-content/uploads/2016/11/C01-G19C.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/a/ab/William_McTaggart_-_Spring_-_Google_Art_Project.jpg",
            "https://www.dorotheum.com/fileadmin/lot-images/38N171205/hires/kuenstler-19.-jahrhundert-203293.jpg",
            "https://img.idesign.vn/2018/04/13/93889/idesign_monalisa_04a.jpg",
            "https://d7hftxdivxxvm.cloudfront.net/?resize_to=width&src=https%3A%2F%2Fartsy-media-uploads.s3.amazonaws.com%2FlG6PgfEukWic566Z_lT3_g%252Fmarron-wynn-picasso-first.jpg&width=1200&quality=80",
            "https://images.saatchiart.com/saatchi/247461/art/3766226/2836110-FSKZGWWW-7.jpg",
            "https://www.artdependence.com/media/5426/5.png",
            "https://i.pinimg.com/originals/f1/d3/43/f1d3435b8bf4f6ed8858dc9670ee49d5.jpg",
            "https://redsvn.net/wp-content/uploads/2018/11/nhung-buc-tranh-son-dau-noi-tieng-hang-dau-viet-nam-3910.jpg",
            "https://vanhocnghethuathatinh.org.vn/images/2019-10-1037765-hinh-anh-vnh.jpg",
            "https://d1fbzwhbgcf4vf.cloudfront.net/optimized-85fdc097bbd3348815cdf392af151123754ebd29a3a4c1c00f6d8364e4effb87.jpeg/800x,q50",
            "https://lh3.googleusercontent.com/proxy/quNj87Iq666Nd595Vk4AI5tfQlW_D8UXY4HGYyANxL08G_f625jXqIsLtEuVhOocXmsqOTTMnYTmNIoewQg9rRjGEWz1wW69IlAPt_0_MctOV2p8Ggv1LtqzCwvjlvQ8mOMP5CvYyg",
            "https://tuhoctiengtrung.vn/wp-content/uploads/2018/10/hinh-anh-tranh-thuy-mac-trung-quoc-co-nghe-thuat-doc-dao-cua-nguoi-tau-2.jpg",
            "https://lh3.googleusercontent.com/proxy/4Wq4HuR0wP97M6fLtQmqK1VtmA6F7RcZODWZfwh5sPFzkBmS1nS4oSnAyQFInNnqmN4YaLoh64vO14ellXyBb4JA6xVtCkLmNIvLuwbnVPnITA",
            "https://lh3.googleusercontent.com/proxy/_Hlnty8wCjFxcpb-rbcbr-JjDSNH-KeTUU_v1sVtS7W4t3KmOT88uWAmxCH8EyzIWxXZ-hcfqXg27qFTD1Ik5r3XqS5qIvfIfE1siS6NQj-KxMELE_GpzGAxK4PEFolsfCXNLDoMtrHrdHwuF2xSFOJvY4QL3PHaUOYdj3rU4lmkQYLPcDjZ_uHLCw6kOFS0qIdMxKNu2yZr9Z8",
            "https://hinhgoc.net/upload/img/_fe-tm-76.jpg?quality=100&width=1200&height=1200",
            "https://doart.com.vn/upload/images/tranh-phong-canh--doart-2(1).jpg",
            "https://lh3.googleusercontent.com/proxy/v6VWnuVnuCTn8TXMa_aNhhgvUvhLQJae16OnZeUrGvN0TX3kNP2I-yhEp4mbpnz7coChjIFn3Jm0dmdmnRFysWGytDun_QFN6XJ7i35j4uIwRr_xGR10",
            "https://upload.wikimedia.org/wikipedia/commons/e/ec/Siege-of-Busanjin-1592.jpg",
            "https://s3-ap-southeast-1.amazonaws.com/images.spiderum.com/sp-images/402ab5d0c3e811e8982bdd77a0c479cc.jpg"
        ]
        describe = "Hội họa là một ngành nghệ thuật trong đó con người sử dụng màu vẽ để tô lên một bề mặt như là giấy, hoặc vải, để thể hiện các ý tưởng nghệ thuật. Thông thường, công việc này do họa sĩ thực hiện. (Họa sĩ là từ dùng để chỉ những người coi hội họa là nghề nghiệp của mình). Kết quả của công việc đó là các tác phẩm hội họa hay còn gọi là các tranh vẽ. Hội họa là một trong những loại hình nghệ thuật quan trọng và phổ biến nhất. Nói cách khác, hội họa là một ngôn ngữ để truyền đạt ý tưởng của người nghệ sĩ bằng các tác phẩm hội họa sử dụng kỹ thuật (nghệ) và phương pháp (thuật) của họa sĩ. Một phần lịch sử hội họa trong nghệ thuật phương Đông lẫn phương Tây bị chi phối bởi nghệ thuật tôn giáo. Ví dụ về các loại tác phẩm này bao gồm các bức tranh miêu tả nhân vật thần thoại trên đồ gốm, các bức tranh tường, trần nhà miêu tả cảnh tượng trong kinh thánh, đến các bức tranh về cuộc đời Đức Phật và các tôn giáo phương Đông khác."

    if category == 'Trang sức':
        links = [
            "https://jemmia.vn/wp-content/uploads/2020/05/hot-xoan-8ly6-gia-bao-nhieu.jpg",
            "https://images-na.ssl-images-amazon.com/images/I/71jBNuLGcQL._SL1500_.jpg",
            "https://specials-images.forbesimg.com/imageserve/5f48454f3e8a7c2ef7185155/960x0.jpg?fit=scale",
            "https://likewatch.com/images/product/large/1ade5f924e776938a0bb6e5367e2f657.jpg",
            "https://cf.shopee.vn/file/659c858d302afcaac2a87b31d75a34b1",
            "https://apj.vn/wp-content/uploads/2019/06/PLT026.jpg",
            "https://longbeachpearl.com/upload/product/1-15345217320A-15346260510.jpg",
            "https://chuyengiakimcuong.com/wp-content/uploads/2020/01/2020-E2584-logo.jpg",
            "https://image.yes24.vn/Upload/ProductImage/TWINKRING2019/2035128_L.jpg",
            "https://i-shop.vnecdn.net/resize/560/560/images/2019/05/22/5ce4c903de515-62-1.jpg",
            "https://preciousle.com/temp/uploaded-day%20chuyen]_nhan-ruby-sao_thumbcr_708x471.png",
            "https://www.hondaviet.vn/wp-content/uploads/2019/06/vong-ngoc-sapphire.jpg",
            "https://cdn.shopify.com/s/files/1/0011/0778/7894/products/jade-gold-ring-1-ame_1024x1024.jpg?v=1544599670",
            "https://www.pnj.com.vn/images/detailed/26/GBD1WA71608.600.jpg",
            "https://salt.tikicdn.com/cache/w1200/ts/product/00/ec/76/8c2bc346a88a58594d4cb3fb98746404.jpg",
            "https://salt.tikicdn.com/cache/w1200/media/catalog/product/e/l/elo1281r_.u5533.d20170802.t120414.830652.jpg",
            "https://cdn.shopify.com/s/files/1/0011/0778/7894/products/bong-tai-da-quy-citrine-es1107-4-ame_36fc00c8-8398-443a-9798-09711841a8da_1024x1024.jpg?v=1586417549",
            "https://trangsucdaquydep.com/wp-content/uploads/2019/05/Da_trang_suc_nhan_tao.jpg"
        ]
        describe = "Trang sức (hay còn gọi là nữ trang, là những đồ dùng trang trí cá nhân, ví dụ như: vòng cổ, nhẫn, vòng đeo tay, khuyên, thường được làm từ đá quý, kim loại quý hoặc các chất liệu khác. Từ trang sức trong tiếng Anh là jewellery bắt nguồn từ jewel được anh hóa từ tiếng Pháp cổ \"jouel\" vào khoảng thế kỷ 13. Nó cũng bắt nguồn từ tiếng Latinh \"jocale\", có nghĩa là đồ chơi. Đồ trang sức là một trong những hình thức trang trí cơ thể cổ xưa nhất. Gần đây người ta đã tìm thấy những chuỗi hạt 100.000 năm tuổi được tin là một trong những món đồ trang sức cổ nhất từng được biết đến."
    
    if category == 'Đồ cổ':
        links = [
            "https://ordi.vn/wp-content/uploads/2019/07/B%E1%BA%A3n-%C4%91%E1%BB%93-b%E1%BB%9D-bi%E1%BB%83n-Vn-1749.jpg",
            "https://blog.travian.com/wp-content/uploads/2017/09/Scavenger_Hunt.png",
            "https://photo-1-baomoi.zadn.vn/w1000_r1/2013_11_05_180_31381742/a3e37c53ad13444d1d02.jpg",
            "https://gomsubaokhanh.vn/media/news/1709_hoa-tiet-hoa-sen.jpg",
            "https://afamilycdn.com/150157425591193600/2020/6/11/-1024x769-1591884534644306267223.jpg",
            "https://anhsontranduc.files.wordpress.com/2015/07/image021.jpg",
            "https://lh3.googleusercontent.com/proxy/_RRRd9bR2KbkiVG6tfVbCclOB8DB8sXhMe5pk7Yg0Rr3YqmNtBf__gDVlK4HjeiQ6prbRBKEJTfUkQxMhn27Eze62PJg6Fn4nUDdGP3kImCNB2C6eprH1BLLCWH9VTjU5_5PoYn1EORVyKh4UUrPaucGg63BVrgAVL0",
            "https://photo-1-baomoi.zadn.vn/w1000_r1/2018_12_07_20_28895686/f65cf92cc36d2a33737c.jpg",
            "https://file.hstatic.net/200000016780/article/3a0b3f8c92736f2d36621_e5fa515c4ce34a3cbbcb3484de80ed3c_1024x1024.jpg",
            "https://vignette.wikia.nocookie.net/disney/images/0/09/Jack_Sparrow%27s_Compass_Opened_and_Closed.png/revision/latest?cb=20140319162333",
            "https://lh3.googleusercontent.com/proxy/IH-np9cpmIA9pWLKehgOFD3gB5IEfK0WOF0uO3S3wNi3GO9ue8o4XcH6b4ngzZc1y56c0TjwMhKWKLIidIz0shu-TTufc7yQxxjCzzqhGJMpOjYwPGq93qi6q0NrPTkLJPyFRPnjJJN5BUCilvLjEodVf6biAQ",
            "https://i.pinimg.com/originals/2b/26/ed/2b26ed2f5441fdc064863034267e4b49.jpg",
            "https://i.pinimg.com/originals/ff/73/c1/ff73c143bf2a01d3eca338f613572cf7.jpg",
            "https://img.chewy.com/is/image/catalog/129810_MAIN._AC_SL1500_V1497970919_.jpg",
            "https://images-na.ssl-images-amazon.com/images/I/91xylgICNyL._AC_SL1500_.jpg",
            "https://cdn0.rubylane.com/_pod/item/1393670/ANCIENTx20Chinesex20Bronzex20Vasex20Qi/Ancient-Chinese-Bronze-Vase-Qing-Dynasty-pic-1A-2048%3A10.10-5b3d21f2-f.jpg",
            "https://cf.shopee.vn/file/4d4e414120285f8140fa74bb0f6a12d8",
            "https://baotangnhanhoc.org/vi/images/stories/CHUM.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Dong_Son_crossbow_trigger.JPG/1280px-Dong_Son_crossbow_trigger.JPG",
            "https://www.thivien.net/attachment/kvTqGUtpQWihq95pFiSZrA.1442028122.jpg"
        ]
        describe = "Một món đồ cổ thực sự (tiếng Latinh : antiquus ; 'old', 'cổ') là một món đồ được coi là có giá trị vì ý nghĩa thẩm mỹ hoặc lịch sử của nó và thường được định nghĩa là ít nhất 100 tuổi (hoặc một số giới hạn khác), mặc dù thuật ngữ thường được sử dụng lỏng lẻo để mô tả bất kỳ đối tượng nào đã cũ. Đồ cổ thường là một món đồ được sưu tầm hoặc được ưa chuộng vì tuổi tác, vẻ đẹp, độ quý hiếm, tình trạng, tiện ích, kết nối tình cảm cá nhân và, hoặc các tính năng độc đáo khác. Nó là một vật thể hiện một thời đại hoặc khoảng thời gian trước đó trong lịch sử loài người. Vintage và sưu tầm được dùng để mô tả những món đồ đã cũ nhưng không đáp ứng tiêu chí 100 năm. Đồ cổ thường là những đồ vật thể hiện một mức độ khéo léo, khả năng sưu tầm hoặc sự chú ý nhất định đến thiết kế, chẳng hạn như bàn làm việc hoặc ô tô đời đầu. Chúng được mua tại các cửa hàng đồ cổ, nơi bán bất động sản, nhà đấu giá, đấu giá trực tuyến và các địa điểm khác, hoặc di sản được thừa kế. Những người buôn bán đồ cổ thường thuộc các hiệp hội thương mại quốc gia, nhiều hiệp hội thuộc CINOA, một liên hiệp các hiệp hội đồ cổ và nghệ thuật trên 21 quốc gia, đại diện cho 5.000 đại lý."

    if category == 'Đồ lưu niệm':
        links = [
            "https://upload.wikimedia.org/wikipedia/vi/8/89/Fifa_world_cup_org.jpg",
            "https://nld.mediacdn.vn/2020/8/23/cup--15981877284481223358625.jpg",
            "https://i.pinimg.com/originals/42/2a/26/422a2600350a3a1256445a6fe4e57507.jpg",
            "https://static.independent.co.uk/s3fs-public/thumbnails/image/2017/05/24/09/rusty-rio-medals.jpg",
            "https://cdn.dnaindia.com/sites/default/files/styles/full/public/2016/07/21/484003-olympicmedalgetty.jpg",
            "https://cdnimg.vietnamplus.vn/t1200/Uploaded/mzdic/2019_12_09/hcv.jpg",
            "https://cdnmedia.webthethao.vn/uploads/img/files/images/fullsize/2019/Th%C3%A1ng%206/11-6/cup.jpg",
            "https://news.otofun.net/stores/news_dataimages/CTV/012019/02/14/3931_2111860-214-jk-3-a9tsl86wgbwno4gjkstf.jpg",
            "https://vcdn-vnexpress.vnecdn.net/2019/01/11/50249855-2289148637771353-1070-3466-6431-1547196592.jpg",
            "https://st.baodatviet.vn/staticFile/Subject/2014/04/28/720p-chelsea%20comp_1__28165369.jpg",
            "https://vietteldng.net/wp-content/uploads/2019/02/Qua-bong-co-chu-ky-cac-danh-thu-VN.jpg",
            "https://znews-photo.zadn.vn/w660/Uploaded/xbhunua/2015_02_14/3.jpg",
            "https://media.baohaiduong.vn/files/library/images/site-1/20190110/web/dau-gia-ao-bong-doi-tuyen-viet-nam-tang-thu-tuong-nguyen-xuan-phuc-40-161110.jpg",
            "https://media.thethao247.vn/upload/thanhtung/2020/05/08/bong-chu-ky-Michael-Jordan-1.jpg",
            "https://images-na.ssl-images-amazon.com/images/I/61mWjm8MvXL._AC_SL1100_.jpg",
            "https://ae01.alicdn.com/kf/HTB1ca0cK3HqK1RjSZFEq6AGMXXa9.jpg",
            "https://i.pinimg.com/originals/9c/e5/21/9ce5213d1c3be9cc2154092b58552e0b.jpg"
        ]
        describe = "Một món quà lưu niệm là một đối tượng mà một người mua lại cho những kỷ niệm mà chủ sở hữu liên kết với nó. Một món quà lưu niệm có thể là bất kỳ vật gì có thể được thu thập hoặc mua và vận chuyển về nhà bởi khách du lịch như một vật lưu niệm của một chuyến viếng thăm. Mặc dù không có chi phí tối thiểu hoặc tối đa nào được yêu cầu tuân thủ khi mua quà lưu niệm, nghi thức sẽ đề nghị giữ nó trong một khoản tiền mà người nhận sẽ không cảm thấy khó chịu khi tặng quà lưu niệm. Bản thân đối tượng có thể có giá trị nội tại, hoặc là biểu tượng của trải nghiệm. Không có đầu vào của chủ sở hữu, ý nghĩa tượng trưng là vô hình và không thể khớp nối."

def openBid():
    return round(random.randint(25000000, 10000000000) + random.randint(0, 90000000)/90000000, 3)

def randomCreateItemDate():
    # namSinh = str(random.randint(2018, 2020))
    # thangSinh = str(random.randint(1, 12))
    # if (len(thangSinh) == 1):
    #     thangSinh = '0' + thangSinh
    # ngaySinh = str(random.randint(1, 28))
    # if (len(ngaySinh) == 1):
    #     ngaySinh = '0' + ngaySinh

    itemYear = str(random.randint(2018, randomCreateDate.namSinh))
    itemMonth = str(random.randint(1, randomCreateDate.thangSinh))
    if (len(itemMonth) == 1):
        itemMonth = '0' + itemMonth
    itemDay = str(random.randint(1, randomCreateDate.ngaySinh))
    if (len(itemDay) == 1):
        itemDay = '0' + itemDay
    return itemDay + '-' + itemMonth + '-' + itemYear

def createCategory():
    arr = ['Thời trang', 'Hội họa', 'Trang sức', 'Đồ cổ', 'Đồ lưu niệm']
    return arr[random.randint(0, len(arr) - 1)]

def itemStatus():
    arr = ['Ready to auction', 'Int Stock', 'Paid', 'Bid success']
    return arr[random.randint(0, len(arr) - 1)]