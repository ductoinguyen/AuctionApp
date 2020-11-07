from datetime import datetime
import time
import app, json
from bson.objectid import ObjectId
from flask import Flask, request, jsonify, render_template, session, redirect, url_for, escape

def filterDate(create_date):
    difference = datetime.now() - datetime.strptime(create_date, "%d/%m/%Y")
    tupleTime = divmod(difference.days * (24*60*60) + difference.seconds, 60)
    return (tupleTime[0]*60 + tupleTime[1])/(24*60*60)

def getAllRequestFromA(id):
    appFlask = app.app
    db = app.db
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y")
    result = [] 
    for item in db.item.find({"id_auctioneer": id}, {"create_date": True, "_id": True}):
        thoiGianChenhLech = filterDate(item["create_date"])
        if thoiGianChenhLech >= 0:
            result.append({
                "id": item["_id"],
                "thoiGianChenhLech": thoiGianChenhLech
            })  
    result = sorted(result, key = lambda item: item["thoiGianChenhLech"])
    if len(result) > 5:
        result = result[:5]
    result = [item["id"] for item in result]
    result = [{
                "id": str(x["_id"]),
                "name": x["name"],
                "price_start": x["price_start"],
                "category": x["category"],
                "create_date": x["create_date"],
                "status": x["status"],
            } for x in db.item.find({"_id": {"$in": result}})]
    return appFlask.response_class(json.dumps(result), mimetype='application/json')    

def getAllRequestFromC():
    appFlask = app.app
    db = app.db
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y")
    result = [] 
    for item in db.item.find({"status": "handling"}, {"create_date": True, "_id": True}):
        thoiGianChenhLech = filterDate(item["create_date"])
        if thoiGianChenhLech >= 0:
            result.append({
                "id": item["_id"],
                "thoiGianChenhLech": thoiGianChenhLech
            })  
    result = sorted(result, key = lambda item: item["thoiGianChenhLech"])
    if len(result) > 5:
        result = result[:5]
    result = [item["id"] for item in result]
    result = [{
                "id": str(x["_id"]),
                "name": x["name"],
                "content": x["content"],
                "image": x["image"],
                "price_start": x["price_start"],
                "category": x["category"],
                "create_date": x["create_date"]
            } for x in db.item.find({"_id": {"$in": result}})]
    return appFlask.response_class(json.dumps(result), mimetype='application/json')

def acceptRequest():
    appFlask = app.app
    db = app.db
    try:
        id_item = request.form['id_item']
        open_bid = request.form['open_bid']
        id_session = request.form['id_session']
    except:
        id_item = request.get_json()['id_item']
        open_bid = request.get_json()['open_bid']
        id_session = request.get_json()['id_session']
    open_bid = open_bid.split("-")
    open_bid = open_bid[2] + "/" + open_bid[1] + "/" + open_bid[0]
    db.item.update({"_id": ObjectId(id_item)}, {"$set": {"open_bid": open_bid, "index_session": id_session}})
    return appFlask.response_class(json.dumps({"result": "ok"}), mimetype='application/json')

def createRequestFromA():
    # điền nốt
    pass

def refuseRequest(id):
    appFlask = app.app
    db = app.db
    db.item.update({"_id": ObjectId(id)}, {"$set": {"status": "fail"}})
    return appFlask.response_class(json.dumps({"result": "ok"}), mimetype='application/json')

def filterItem():
    appFlask = app.app
    db = app.db
    try:
        open_bid = request.form['open_bid']
        index_session = request.form['index_session']
        category = request.form['category']
    except:
        open_bid = request.get_json()['open_bid']
        index_session = request.get_json()['index_session']
        category = request.get_json()['category']
    open_bid = open_bid.split("-")
    open_bid = open_bid[2] + "/" + open_bid[1] + "/" + open_bid[0]
    index_session = int(index_session)
    category = {"thoitrang": "Thời trang", "hoihoa": "Hội họa", "trangsuc": "Trang sức", "doluuniem": "Đồ lưu niệm", "doco": "Đồ cổ"}[category]
    # print(open_bid, index_session, category)
    # # results = 
    data = []
    for item in db.item.find({"open_bid": open_bid, "index_session": index_session, "category": category}):
        try: 
            if item["status"] == "fail" or item["status"] == "handling":
                continue
            name_auctioneer = [x["name"] for x in db.auctioneer.find({"_id": ObjectId(str(item["id_auctioneer"]))}, {"name"}).limit(1)][0]
            content = {
                "id_item": str(item["_id"]),
                "name": item["name"],
                "price_start": item["price_start"],
                "name_auction": name_auctioneer,
                "image": item["image"]
            }
            if item["status"] == "ready to auction":
                if item["price_start"] == item["price_max"]:
                    content.update({"status": "Chưa đấu giá"})
                else:
                    name_bidder = [x["name"] for x in db.bidder.find({"_id": ObjectId(str(item["id_bidder"]))}, {"name"}).limit(1)][0]    
                    content.update({"status": "Đang đấu giá", "price_max": item["price_max"], "name_bidder": name_bidder})
            elif item["status"] == "paid":
                name_bidder = [x["name"] for x in db.bidder.find({"_id": ObjectId(str(item["id_bidder"]))}, {"name"}).limit(1)][0]    
                content.update({"status": "Đã đấu giá", "price_max": item["price_max"], "name_bidder": name_bidder})
            else:
                content.update({"status": "Đấu giá thất bại"})
            print(content)
            data.append(content)
        except:
            continue
    # print(data)
    return appFlask.response_class(json.dumps(data), mimetype='application/json')