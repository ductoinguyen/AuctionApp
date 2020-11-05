from datetime import datetime
import time
import app, json
from bson.objectid import ObjectId
from flask import Flask, request, jsonify, render_template, session, redirect, url_for, escape

def createIndexRoom():
    return {"thoitrang": 0, "hoihoa": 1, "trangsuc": 2, "doluuniem": 3, "doco": 4}
        
def getTime():
    now = datetime.now()
    return (now.strftime("%d/%m/%Y"), int(now.strftime("%H")))

def initTimeRoom():
    now = datetime.now()
    duration = 3600 - (int(now.strftime("%M"))*60 + int(now.strftime("%S")))
    return [(now, duration) for _ in range(5)]
    
def differenceTime(first, second):
    difference = second - first
    return divmod(difference.days * (24*60*60) + difference.seconds, 60)
    # return a tuple(min, sec)

def checkTimeRemaining(typeroom):
    now = datetime.now()
    time_room = app.timeRoom[app.indexRoom[typeroom]]
    diffTime = differenceTime(time_room[0], now)
    appFlask = app.app
    db = app.db
    if time_room[1] <= diffTime[0]*60 + diffTime[1]:
        try:
            typeroom = typeroom.strip()
            id_item = str(app.primaryItemId[app.indexRoom[typeroom]])
            try:
                x = [x for x in db.item.find({"_id": ObjectId(id_item)}, {"id_bidder": True, "price_max": True}).limit(1)][0]
                db.bidder.update_one({"_id": ObjectId(x["id_bidder"])}, {"$inc": {"accountBalance": - x["price_max"]}}) 
                db.item.update_one({"_id": ObjectId(id_item)}, {"$set": {"status": "paid"}})
            except:
                db.item.update_one({"_id": ObjectId(id_item)}, {"$set": {"status": "fail-auction"}})
            duration = 3600 - int(now.strftime("%M"))*60 + int(now.strftime("%S"))
            app.timeRoom[app.indexRoom[typeroom]] = (now, duration)     
        except:
            1
    time_room = app.timeRoom[app.indexRoom[typeroom]]
    diffTime = differenceTime(time_room[0], now)
    timeRemaining = time_room[1] - (diffTime[0]*60 + diffTime[1])
    mins = timeRemaining // 60
    mins = '0' + str(mins) if mins < 10 else str(mins)
    secd = timeRemaining % 60
    secd = '0' + str(secd) if secd < 10 else str(secd)
    # print(mins + ":" + secd)
    return (mins + ":" + secd)

def getTimeRoom(typeroom):
    (dt_string, duration) = [(x["start"], x["duration"]) for x in  app.db.time_room.find({"name": typeroom})][0]
    return (datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S"), duration)

def checkTimeRemainingDB(typeroom):
    appFlask = app.app
    db = app.db
    now = datetime.now()
    time_room = getTimeRoom(typeroom)
    diffTime = differenceTime(time_room[0], now)
    if time_room[1] <= diffTime[0]*60 + diffTime[1]:
        try:
            typeroom = typeroom.strip()
            id_item = str(app.primaryItemId[app.indexRoom[typeroom]])
            try:
                x = [x for x in db.item.find({"_id": ObjectId(id_item)}, {"id_bidder": True, "price_max": True}).limit(1)][0]
                db.bidder.update_one({"_id": ObjectId(x["id_bidder"])}, {"$inc": {"accountBalance": - x["price_max"]}}) 
                db.item.update_one({"_id": ObjectId(id_item)}, {"$set": {"status": "paid"}})
            except:
                db.item.update_one({"_id": ObjectId(id_item)}, {"$set": {"status": "fail-auction"}})
            duration = 3600 - int(now.strftime("%M"))*60 + int(now.strftime("%S"))
            db.time_room.update({"name": typeroom}, {"$set": {"start": now.strftime("%d/%m/%Y %H:%M:%S"), "duration": duration}})    
        except:
            1
    time_room = getTimeRoom(typeroom)
    diffTime = differenceTime(time_room[0], now)
    timeRemaining = time_room[1] - (diffTime[0]*60 + diffTime[1])
    mins = timeRemaining // 60
    mins = '0' + str(mins) if mins < 10 else str(mins)
    secd = timeRemaining % 60
    secd = '0' + str(secd) if secd < 10 else str(secd)
    # print(mins + ":" + secd)
    return (mins + ":" + secd)

def updateTimeRemainingDB(item_category, typeroom):
    indexCategories = {"Thời trang": 0, "Hội họa": 1, "Trang sức": 2, "Đồ lưu niệm": 3, "Đồ cổ": 4}
    now = datetime.now()
    duration = 3600 - (int(now.strftime("%M"))*60 + int(now.strftime("%S")))
    app.db.time_room.update({"name": typeroom}, {"$set": {"start": now.strftime("%d/%m/%Y %H:%M:%S"), "duration": duration}})
    # app.timeRoom[indexCategories[item_category]] = (now, min(5*60, duration))

def bid(typeroom):
    appFlask = app.app
    db = app.db
    id_bidder = session["id"]
    username = session["username"]
    try:
        price = request.form['price']
        id_item = request.form['id_item']
    except:
        price = request.get_json()["price"]
        id_item = request.get_json()["id_item"]        
    (max_price_current, item_name, item_category) = [(x["price_max"], x["name"], x["category"]) for x in db.item.find({"_id": ObjectId(id_item)}, {"price_max": True, "name": True, "category": True})][0]
    
    # price khi submit nhỏ hơn price_max hien tai => that bai!
    price = int("".join(str(price).split(",")))
    if price <= max_price_current:
        return appFlask.response_class(json.dumps({"result": "Cần đấu giá cao hơn giá cao nhất hiện tại"}),mimetype='application/json')
    
    # kiem tra so du tai khoan
    accountBalance = [x["accountBalance"] for x in db.bidder.find({"_id": ObjectId(id_bidder)}, {"accountBalance": True})][0]
    if accountBalance < price:
        return appFlask.response_class(json.dumps({"result": "Số dư tài khoản không đủ"}),mimetype='application/json')
    
    # dau gia thuc su
    db.item.update({"_id": ObjectId(id_item)}, {"$set": {"price_max": price, "id_bidder": id_bidder}})
    # luu lich su dau gia
    db.bidder_history.insert({"id_bidder": id_bidder, "status": "auction", "id_item": id_item, "item_name": item_name, "item_category": item_category, "price": price})
    updateTimeRemainingDB(item_category, typeroom)
    return appFlask.response_class(json.dumps({"result": "Thành công"}),mimetype='application/json')

# dung trong file bid, update clock khi co nguoi dau gia moi
def updateTimeRemaining(item_category):
    indexCategories = {"Thời trang": 0, "Hội họa": 1, "Trang sức": 2, "Đồ lưu niệm": 3, "Đồ cổ": 4}
    now = datetime.now()
    duration = 3600 - (int(now.strftime("%M"))*60 + int(now.strftime("%S")))
    app.timeRoom[indexCategories[item_category]] = (now, min(5*60, duration))
    # //////////////////////////// 5 phut ///////////////////////

# tim gio cua file category
def timeRemaining():
    appFlask = app.app
    try: 
        now = datetime.now()
        timeRemaining = 3600 - (int(now.strftime("%M"))*60 + int(now.strftime("%S")))
        mins = timeRemaining // 60
        mins = '0' + str(mins) if mins < 10 else str(mins)
        secd = timeRemaining % 60
        secd = '0' + str(secd) if secd < 10 else str(secd)
        return appFlask.response_class(json.dumps({"timeRemaining": mins + ":" + secd}), mimetype='application/json')
    except:
        return appFlask.response_class(json.dumps({"timeRemaining": "00:00"}), mimetype='application/json')
    
def getItemInRoom(loaiphong):
    appFlask = app.app
    db = app.db
    category = {"thoitrang": "Thời trang", "hoihoa": "Hội họa", "trangsuc": "Trang sức", "doluuniem": "Đồ lưu niệm", "doco": "Đồ cổ"}
    type_room = category[loaiphong]
    (currentDate, currentHour) = getTime()
    x = [x for x in db.item.find({"open_bid": currentDate, "status": "ready to auction", "category": type_room, "index_session": currentHour}, {"_id": True, "image": True}).limit(3)]
    if len(x) == 0:
        return appFlask.response_class(json.dumps([{"status": "NULL"}]), mimetype='application/json')
    data = [{"id_item": str(i["_id"]), "image": i["image"]} for i in x]
    data.append({"status": "HAVE"})
    return appFlask.response_class(json.dumps(data), mimetype='application/json')
           

def createRoom(typeroom):
    appFlask = app.app
    db = app.db
    now = datetime.now()
    start = now.strftime("%d/%m/%Y %H:%M:%S")
    duration = 3600 - (int(now.strftime("%M"))*60 + int(now.strftime("%S")))
    db.time_room.update({"name": typeroom}, {"$set": {"start": start, "duration": duration}})
    return appFlask.response_class(json.dumps({"result": "ok"}), mimetype='application/json')

def getPricemaxTimedb(typeroom):
    appFlask = app.app
    db = app.db
    try:    
        typeroom = typeroom.strip()
        category = {"thoitrang": "Thời trang", "hoihoa": "Hội họa", "trangsuc": "Trang sức", "doluuniem": "Đồ lưu niệm", "doco": "Đồ cổ"}
        type_room = category[typeroom]
        x = [x for x in db.item.find({"_id": ObjectId(str(app.primaryItemId[app.indexRoom[typeroom]]))}, {"price_max": True, "id_bidder": True})][0]
        try:
            flagTop1Bidder = 1 if x["id_bidder"] == session["id"] else 0
        except:
            flagTop1Bidder = 0
        return appFlask.response_class(json.dumps({"status": "SUC", "timeRemaining": checkTimeRemainingDB(typeroom), "price_max": x["price_max"], "flagTop1Bidder": flagTop1Bidder}),mimetype='application/json')
    except:
        return appFlask.response_class(json.dumps({"status": "ERR"}),mimetype='application/json')

# first = datetime.now()
# time.sleep(130)
# second = datetime.now()
# print(differenceTime(first, second))


# from datetime import datetime
# now = datetime.now()
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print(dt_string)
# datetime_object = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")