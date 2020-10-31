from datetime import datetime
import time
import app
from bson.objectid import ObjectId

def createIndexRoom():
    return {"thoitrang": 0, "hoihoa": 1, "trangsuc": 2, "doluuniem": 3, "doco": 4}
        
def getTime():
    now = datetime.now()
    return (now.strftime("%d/%m/%Y"), int(now.strftime("%H")))

def initTimeRoom():
    now = datetime.now()
    duration = 3600 - int(now.strftime("%M"))*60 + int(now.strftime("%S"))
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
    if time_room[1] <=  diffTime[0]*60 + diffTime[1]:
        try:
            typeroom = typeroom.strip()
            id_item = str(app.primaryItemId[app.indexRoom[typeroom]])
            db.item.update_one({"_id": ObjectId(id_item)}, {"$set": {"status": "paid"}})
            x = [x for x in db.item.find({"_id": ObjectId(id_item)}, {"id_bidder": True, "price_max": True}).limit(1)][0]
            db.bidder.update_one({"_id": ObjectId(x)}, {"$inc": {"accountBalance": - x["price_max"]}})  
            duration = 3600 - int(now.strftime("%M"))*60 + int(now.strftime("%S"))
            app.timeRoom[app.indexRoom[typeroom]] = (now, duration)     
        except:
            1
    timeRemaining = time_room[1] - (diffTime[0]*60 + diffTime[1])
    return str(timeRemaining // 60) + ":" + str(timeRemaining % 60)

def updateTimeRemaining(item_category):
    indexCategories = {"Thời trang": 0, "Hội họa": 1, "Trang sức": 2, "Đồ lưu niệm": 3, "Đồ cổ": 4}
    app.timeRoom[indexCategories[item_category]] = (datetime.now(), 5*60)
        

# first = datetime.now()
# time.sleep(130)
# second = datetime.now()
# print(differenceTime(first, second))