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
    diffTime = differenceTime(time_room[0], now)
    timeRemaining = time_room[1] - (diffTime[0]*60 + diffTime[1])
    mins = timeRemaining // 60
    mins = '0' + str(mins) if mins < 10 else str(mins)
    secd = timeRemaining % 60
    secd = '0' + str(secd) if secd < 10 else str(secd)
    # print(mins + ":" + secd)
    return (mins + ":" + secd)


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
           


# first = datetime.now()
# time.sleep(130)
# second = datetime.now()
# print(differenceTime(first, second))