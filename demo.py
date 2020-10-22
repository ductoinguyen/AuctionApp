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
        arr = [
            "Giày da đầu tiên tìm thấy ở một hang động của Armenia năm 2008 có niên đại 5.500 năm TCN; đôi giày này là một mảnh da bò với dây da buộc.",
            "Giày của người băng Ốtzi có niên đại 3.300 năm TCN; nó đặc trưng bởi màu nâu da gấu với da ở mặt bên và chuỗi vỏ cây ở mu bàn chân thắt chặt lại.",
            "Giày của mọi da đỏ của người da đỏ ở Nam Mỹ, là những đôi giày bó sát, có đế mềm, làm từ da, da bò bizon và có trang trí; tuy nhiên, chúng rất dễ ngấm nước, vì vậy những người da đỏ thường đi chân trần vào mùa hạ hoặc trong thời tiết ẩm ướt.",
            "Trang phục của nam giới rất đơn giản, gọi là shendyt, chỉ là một cái váy quấn quanh thắt lưng, đôi khi được xếp ly hoặc chụm về phía trước và thường để mình trần. Váy shendyt thời kỳ Cổ vương quốc rất ngắn, sang thời kỳ Trung vương quốc, nó dài hơn, có khi phủ cả mắt cá chân. Những người đàn ông (kể cả phụ nữ) thuộc tầng lớp quý tộc thường khoác lên mình một áo choàng mỏng có ống tay dài bằng vải lanh và được xếp li. Dây thắt lưng của họ thường được gắn thêm những tua rua để trang trí. Vào cuối thời kỳ này, một chiếc khố hình tam giác được mặc bên trong lớp váy ngoài. Một điều đặc biệt là đàn ông lúc bấy giờ lại có ý thức về thời trang hơn cả phụ nữ. Từ những bức phù điêu trên các ngôi mộ, người ta có thể ước lượng rằng, có hơn 40 kiểu loại trang phục dành cho đàn ông.",
            "Trong suốt thời kỳ cổ đại, phụ nữ Ai Cập chủ yếu chỉ mặc một loại váy bó sát cơ thể, gọi là kalasiris. Một mảnh vải dài sẽ được gấp và khâu lại tạo thành một cái váy ống, kéo dài từ trên mắt cá chân cho đến dưới hoặc trên ngực. Một cái váy kalasiris thường có một hoặc hai dây để giữ trên vai. Phụ nữ Ai Cập xưa kia không coi việc để ngực trần là điều khiếm nhã. Phụ nữ (kể cả đàn ông) thường đeo nhiều vòng hạt trên cổ hoặc đơn giản là những chiếc khăn quàng đầy màu sắc, và cũng mặc một áo choàng bằng vải lanh với hình thức tương tự như đàn ông. Trong các tác phẩm nghệ thuật, váy kalasiris thường được mô tả là bó sát vào cơ thể của người phụ nữ, kể cả khi họ quỳ hoặc ngồi. Thực tế là vải lanh có độ giãn. Vì vậy, trang phục bằng vải lanh sẽ có xu hướng rộng thùng thình chứ không phải ôm sát cơ thể như trong nghệ thuật."
        ]

    if category == 'Hội họa':
        arr = [
            "Mona Lisa (La Gioconda hay La Joconde, Chân dung Lisa Gherardini, vợ của Francesco del Giocondo) là một bức chân dung thế kỷ 16 được vẽ bằng sơn dầu trên một tấm gỗ dương tại Florence bởi Leonardo da Vinci trong thời kì Phục Hưng Italia. Tác phẩm thuộc sở hữu của Chính phủ Pháp và hiện được trưng bày tại bảo tàng Louvre ở Paris, Pháp với tên gọi Chân dung Lisa Gherardini, vợ của Francesco del Giocondo. Bức tranh là một bức chân dung nửa người và thể hiện một phụ nữ có những nét thể hiện trên khuôn mặt thường được miêu tả là bí ẩn. Sự mơ hồ trong nét thể hiện của người mẫu, sự lạ thường của thành phần nửa khuôn mặt, và sự huyền ảo của các kiểu mẫu hình thức và không khí hư ảo là những tính chất mới lạ góp phần vào sức mê hoặc của bức tranh. Có lẽ nó là bức tranh nổi tiếng nhất từng bị đánh cắp và được thu hồi về bảo tàng Louvre. Ít tác phẩm nghệ thuật khác từng là chủ đề của nhiều sự chăm sóc kỹ lưỡng, nghiên cứu, thần thoại hoá và bắt chước tới như vậy. Một sự nghiên cứu và vẽ thử bằng chì than và graphite về Mona Lisa được cho là của Leonardo có trong Bộ sưu tập Hyde, tại Glens Falls, NY.",
            "Tiếng thét (tiếng Na Uy: Skrik) là tên của một trong bốn bản sáng tác, dưới dạng tranh vẽ và in trên đá theo trường phái biểu hiện của danh họa người Na Uy Edvard Munch vào khoảng năm 1893 và 1910. Tất cả các bức họa đều vẽ một nhân vật đầy âu lo tuyệt vọng tương phản với phong cảnh hòa cùng bầu trời đỏ. Họa sĩ không chú tâm mô tả cái mình nhìn thấy, ghét sự hời hợt của tình cảm. Chủ đích của ông là biểu hiện mạnh nhất, nhanh nhất tình cảm mạnh mẽ, tức thời của mình. Thế nên tranh nghiêng ngả, không cân bằng, nét vung mạnh mẽ, chói gắt. Phong cảnh nền trong bức tranh thuộc thành phố Oslofjord, nhìn từ Ekeberg, Oslo. Edvard Munch tạo ra bốn bản của Tiếng thét trên các chất liệu khác nhau. Phòng trưng bày quốc gia Na Uy ở Oslo giữ một trong hai bức họa vẽ bằng thuốc màu (năm 1893, là bức tranh ở bên phải). Viện bảo tàng Munch giữ một bản khác (bản năm 1910) và một bản phấn màu. Bản thứ tư (phấn màu, năm 1895) được một người mua với trị giá 119.922.500 đôla tại cuộc bán đấu giá Mỹ thuật Ấn tượng và Hiện đại do tập đoàn Sotheby's tổ chức vào ngày 2 tháng 5 năm 2012, là bức tranh có mức giá danh định cao nhất từ trước đến nay trong một cuộc đấu giá. Bức tranh Những Người Chơi Bài của danh họa Paul Cézanne được bán bí mật vào năm 2011 với trị giá hơn 250 triệu đô la",
            "Chân dung tự họa là một bức tranh sơn dầu năm 1889 vẽ bởi họa sĩ Hậu ấn tượng người Hà Lan Vincent van Gogh. Bức tranh, có thể là bức chân dung tự họa cuối cùng của Van Gogh, được vẽ vào tháng 9 năm đó, ngay trước khi ông rời Saint-Rémy-de-Provence ở miền nam nước Pháp.",
            "Salvator Mundi là bức tranh củahọa sĩ người Ý thời Phục hưng Leonardo da Vinci có niên đại c. 1500. Từ lâu được cho là bản sao của một bản gốc bị mất với lớp sơn quá dày , nó đã được tái khám phá, phục hồi và đưa vào một cuộc triển lãm lớn của Leonardo tại Phòng trưng bày Quốc gia , London, vào năm 2011–12. Christie's tuyên bố ngay sau khi bán tác phẩm mà hầu hết các học giả hàng đầu coi đó là tác phẩm gốc của Leonardo, nhưng sự ghi nhận này đã bị các chuyên gia khác tranh cãi, một số người cho rằng ông chỉ đóng góp một số yếu tố nhất định. Bức tranh mô tả Chúa Giê-su trong trang phục thời Phục hưng , làm dấu thánh giá bằng tay phải, trong khi cầm một quả cầu pha lê trong suốt, không khúc xạ ở bên trái, báo hiệu vai trò của ngài là Salvator Mundi (tiếng Latinh có nghĩa là 'Cứu thế giới') và đại diện cho 'thiên cầu' của các tầng trời. Khoảng 20 biến thể khác của tác phẩm được biết đến bởi các sinh viên và tín đồ của Leonardo.",
            "Interchange , còn được gọi là đổi chổ lẫn nhau , là một dầu trên vải vẽ bởi người Hà Lan-Mỹ biểu hiện trừu tượng họa sĩ Willem de Kooning (1904-1997). Nó có kích thước 200,7 x 175,3 cm (79,0 x 69,0 in) và được hoàn thành vào năm 1955. Đây là một trong những phong cảnh trừu tượng đầu tiên của de Kooning, và đánh dấu sự thay đổi trong phong cách của ông dưới ảnh hưởng của nghệ sĩ đồng nghiệp Franz Kline. Vào tháng 9 năm 2015, nó đã được David Geffen Foundation bán cho Kenneth C. Griffin với giá 300 triệu đô la (tương đương 325.731.065,70 đô la vào năm 2019), một mốc mới cho mức giá cao nhất từ ​​trước đến nay cho một bức tranh, cho đến tháng 11 năm 2017 bởi Salvator Mundi của Leonardo Da Vinci. Nó đã được cho mượn tại Viện Nghệ thuật Chicago."
        ]

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
        arr = [
            "Đồ trang sức rất phổ biến ở Ai Cập cổ đại, bất kể tầng lớp xã hội nào, vì chúng cũng được xem là bùa hộ mệnh. Chúng là những thứ như bông tai, dây chuyền, vòng đeo tay chân và nhẫn. Số lượng đồ trang sức của một cá nhân thường chỉ ra vị trí xã hội và mức độ giàu có của họ. Trang sức bằng vàng và các loại đá quý được dành cho những người có địa vị cao quý; trong khi những người nghèo thường đeo những trang sức bằng gốm nhiều màu. Các pharaon và những thành viên trong hoàng gia tự phân biệt mình với dân thường bằng những món trang sức khá lộng lẫy, đặc biệt, chúng đều được trang trí với uraeus - biểu tượng uy quyền của nhà vua. Vàng được khai thác với số lượng lớn, tập trung tại vùng sa mạc phía đông hoặc đến từ Nubia. Bạc được cho là khá hiếm đối với người Ai Cập bởi vì chúng được nhập từ bên châu Á. Vì thế mà bạc lại quý hơn vàng. Những loại đá bán quý như carnelian, jasper hay thạch anh tím được khai thác từ các mỏ đá ở sa mạc phía đông; trong khi quặng đá ngọc lam nằm ở bán đảo Sinai và ngọc lưu ly xanh thẫm lại nằm ở vùng Afghanistan xa xôi. Thủy tinh và sứ cũng được ưa thích vì chúng có thể chế tác ra những món trang sức đa dạng sắc màu.",
            "Viên kim cương Hope là một trong những món đồ trang sức nổi tiếng nhất thế giới, với lý lịch quyền sở hữu có niên đại gần bốn thế kỷ. Màu xanh lam hiếm hoi được ngưỡng mộ do một lượng nhỏ nguyên tử boron. Với trọng lượng 45,52 cara, kích thước đặc biệt của viên kim cương đã tiết lộ những phát hiện mới về sự hình thành đá quý. Món trang sức được cho có nguồn gốc từ Ấn Độ, được biết đến đã cắt gọt từ viên Màu Xanh nước Pháp (Le bleu de France), dâng nộp lên vua Louis XIV. Người ta thu nhận tên nó khi xuất hiện trong danh mục sưu tập đá quý thuộc sở hữu của một gia đình ngân hàng London gọi là Hope năm 1839. Sau đó viên kim cương được bán cho nhà xã hội Washington Evalyn Walsh McLean thường đeo viên kim cương lên người.",
            "Trang sức (hay còn gọi là nữ trang, là những đồ dùng trang trí cá nhân, ví dụ như: vòng cổ, nhẫn, vòng đeo tay, khuyên, thường được làm từ đá quý, kim loại quý hoặc các chất liệu khác. Từ trang sức trong tiếng Anh là jewellery bắt nguồn từ jewel được anh hóa từ tiếng Pháp cổ 'jouel' vào khoảng thế kỷ 13. Nó cũng bắt nguồn từ tiếng Latinh 'jocale', có nghĩa là đồ chơi. Đồ trang sức là một trong những hình thức trang trí cơ thể cổ xưa nhất. Gần đây người ta đã tìm thấy những chuỗi hạt 100.000 năm tuổi được tin là một trong những món đồ trang sức cổ nhất từng được biết đến.",
            "Kim cương là một trong hai dạng thù hình được biết đến nhiều nhất của cacbon, có độ cứng rất cao và khả năng khúc xạ cực tốt làm cho nó có rất nhiều ứng dụng trong cả công nghiệp và ngành kim hoàn. Kim cương được cho là một loại khoáng sản với những tính chất vật lý hoàn hảo.",

        ]
    
    if category == 'Đồ cổ':
        links = [

        ]
        arr = [
            
        ]

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
        arr = [
            "Chiếc áo đội tuyển có chữ ký của HLV Park Hang Seo và các tuyển thuỷ Việt Nam vừa giành chức vô địch AFF Cup 2018",
            "Cuộc thi lựa chọn chiếc cúp thay thế đã được tổ chức bởi FIFA để chuẩn bị cho World Cup 1974. Chiếc cúp cao 36,5 cm (14,4 in), được làm từ 5 kg (11 lb) vàng 18 carat (tỷ lệ 75% vàng) với đế có đường kính 13 cm (5,1 in) gồm hai lớp đá xanh (malachit). Chiếc cúp được yêu cầu làm rỗng; do nếu nó được làm đặc, nó sẽ nặng tới 70–80 kg và quá nặng để có thể giương cao chiếc cúp. Bertoni, Milano là người chế tác chiếc cúp, với tổng khối lượng là 6,175 kg (13,6 lb), trị giá 200.000 USD với biểu tượng hai người đang giữ Trái Đất. Gazzaniga đã miêu tả cúp như các đường bật lên từ đáy, vươn lên theo đường xoắn ốc, mở rộng ra để đón lấy thế giới. Nghệ thuật điêu khắc làm nổi bật lên hình người nhỏ gọn vươn lên thanh thoát, hiện ra hình ảnh hai vận động viên trong thời khắc tưng bừng của chiến thắng. Thủ quân của đội tuyển Tây Đức, Franz Beckenbauer là người đầu tiên giương cao chiếc cúp tại World Cup 1974. Chiếc cúp có khắc chữ nổi 'FIFA World Cup' tại đế của nó. Tên của nước có đội tuyển giành chức vô địch tại mỗi kỳ World Cup được khắc tại mặt đáy của cúp, nên sẽ không nhìn thấy được khi đặt chiếc cúp thẳng đứng. Câu ghi năm giải đấu diễn ra và tên của đội tuyển quốc gia vô địch đều được khắc bằng tiếng của quốc gia đó,ví dụ '— 1990 Deutschland' và '— 1994 Brasil' (tuy nhiên, năm 2010 nhà vô địch được khắc bằng tiếng Anh mà không phải bằng tiếng Tây Ban Nha theo quy định). Cho đến năm 2018, mười hai nhà vô địch đã được khắc ở đế. Chưa rõ FIFA sẽ dừng sử dụng chiếc cúp này như thế nào sau khi tên đội tuyển và năm giải đấu đã diễn ra được khắc đầy lên đáy của cúp; điều này sớm nhất sẽ không xảy ra sau World Cup 2030. Nghị quyết hiện nay của FIFA khẳng định rằng chiếc cúp này không giống như cái đầu tiên, không thể giữ được mãi mãi: đội vô địch chỉ nhận được bản sao mạ vàng chứ không phải chiếc cúp bằng vàng nguyên khối như chiếc cúp thật."
        ]

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