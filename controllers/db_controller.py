import pymongo
from pymongo import MongoClient
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process 
import os
import threading
from bson.objectid import ObjectId
from flask import Flask, request, jsonify, render_template, session, redirect, url_for, escape
import app
from models import room
import os, json, threading, time
from datetime import date
from models import room

def getDB():
    MONGO_URL = os.environ.get('MONGO_URL')
    if not MONGO_URL:
        MONGO_URL = "mongodb+srv://hequantri:hequantri@cluster0.q0gxn.gcp.mongodb.net/auctionDB?retryWrites=true&w=majority";
    myclient = MongoClient(MONGO_URL)
    db = myclient["auctionDB"]
    # print('ok')
    return db

def checkLogin(db, username, password):
    result = (db.auctioneer.find({"username": username, "password": password}, {"_id": True, "name": True}))
    x = []
    for x in result:
        break
    if len(x) > 0:
        return (x['_id'], "auctioneer", x["name"])
    result = (db.bidder.find({"username": username, "password": password}, {"_id": True, "name": True}))
    for x in result:
        break
    if len(x) > 0:
        return (x['_id'], "bidder", x["name"])
    result = (db.admin.find({"username": username, "password": password}, {"_id": True, "name": True}))
    for x in result:
        break
    if len(x) > 0:
        return (x['_id'], "admin", x["name"])
    return -1

def checkAccount(db, username):
    try:
        result = (db.auctioneer.find({"username": username}, {"_id": True}))
        x = []
        for x in result:
            break
        if len(x) > 0:
            return -1
        result = (db.bidder.find({"username": username}, {"_id": True}))
        for x in result:
            break
        if len(x) > 0:
            return -1
        result = (db.admin.find({"username": username}, {"_id": True}))
        for x in result:
            break
        if len(x) > 0:
            return -1
        return 0
    except:
        return -1


# ben B tra gia san pham qua method POST
def bid():
    appFlask = app.app
    db = app.db
    # try:
    id_bidder = session["id"]
    username = session["username"]
    # parameter co price va id_item
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
    room.updateTimeRemaining(item_category)
    return appFlask.response_class(json.dumps({"result": "Thành công"}),mimetype='application/json')
    # except:
    #     return appFlask.response_class(json.dumps({"result": "Thất bại"}),mimetype='application/json')

def getAccountBalance():
    appFlask = app.app
    db = app.db
    id_bidder = session["id"]
    accountBalance = [x["accountBalance"] for x in db.bidder.find({"_id": ObjectId(id_bidder)}, {"accountBalance": True})][0]
    return appFlask.response_class(json.dumps({"status": "SUC", "accountBalance": accountBalance}),mimetype='application/json')

def getPrimaryItemInRoom(typeroom):
    appFlask = app.app
    db = app.db
    try:    
        typeroom = typeroom.strip()
        (currentDate, currentHour) = room.getTime()
        category = {"thoitrang": "Thời trang", "hoihoa": "Hội họa", "trangsuc": "Trang sức", "doluuniem": "Đồ lưu niệm", "doco": "Đồ cổ"}
        type_room = category[typeroom]
        x = [x for x in db.item.find({"open_bid": currentDate, "status": "ready to auction", "category": type_room, "index_session": currentHour}).limit(1)][0]
        app.primaryItemId[app.indexRoom[typeroom]] = str(x["_id"])
        return appFlask.response_class(json.dumps({"status": "SUC", "id_item": str(x["_id"]), "title": x["name"], "description": x["content"], "image": x["image"], "price_start": x["price_start"], "price_max": x["price_max"], "id_auctioneer": str(x["id_auctioneer"])}),mimetype='application/json')
    except:
        return appFlask.response_class(json.dumps({"status": "ERR"}),mimetype='application/json')

def getInfoItem(id):
    appFlask = app.app
    db = app.db
    try:
        x = [x for x in db.item.find({"_id": ObjectId(id)}).limit(1)][0]
        return appFlask.response_class(json.dumps({"status": "SUC", "title": x["name"], "description": x["content"], "image": x["image"], "price_start": x["price_start"], "id_auctioneer": str(x["id_auctioneer"]), "date": x["open_bid"], "hour": x["index_session"]}),mimetype='application/json')
    except:
        return appFlask.response_class(json.dumps({"status": "ERR"}),mimetype='application/json')

def getInfoAuctioneer(id):
    appFlask = app.app
    db = app.db
    try:
        x = [x for x in db.auctioneer.find({"_id": ObjectId(id)}).limit(1)][0]
        return appFlask.response_class(json.dumps({"status": "SUC", "name": x["name"], "phoneNumber": x["phoneNumber"], "address": x["address"]}),mimetype='application/json')
    except:
        return appFlask.response_class(json.dumps({"status": "ERR"}),mimetype='application/json')
    
def nextItem(typeroom):
    appFlask = app.app
    db = app.db
    try:
        typeroom = typeroom.strip()
        (currentDate, currentHour) = room.getTime()
        # print(currentDate, currentHour)
        category = {"thoitrang": "Thời trang", "hoihoa": "Hội họa", "trangsuc": "Trang sức", "doluuniem": "Đồ lưu niệm", "doco": "Đồ cổ"}
        type_room = category[typeroom]
        result = db.item.find({"open_bid": currentDate, "status": "ready to auction", "category": type_room, "index_session": currentHour}, {"_id": True, "image": True}).skip(1)
        data = [{"status": "SUC"}]
        for x in result:
            data.append({
                "id_item": str(x["_id"]),
                "image": x["image"]
            })
        return appFlask.response_class(json.dumps(data),mimetype='application/json')
    except:
        return appFlask.response_class(json.dumps([{"status": "ERR"}]),mimetype='application/json')

def checkToSaveInfo(id):
    session["id_item"] = id
    appFlask = app.app
    db = app.db
    try:
        if 'username' in session and session["type_account"] == "bidder":
            (max_price_current, item_name, item_category) = [(x["price_max"], x["name"], x["category"]) for x in db.item.find({"_id": ObjectId(id)}, {"price_max": True, "name": True, "category": True})][0]
            db.bidder_history.insert({"id_bidder": str(session["id"]), "status": "readinfo", "id_item": id, "item_name": item_name, "item_category": item_category, "price": max_price_current})
    except:
        return   

def getPricemaxTime(typeroom):
    appFlask = app.app
    db = app.db
    try:    
        typeroom = typeroom.strip()
        (currentDate, currentHour) = room.getTime()
        category = {"thoitrang": "Thời trang", "hoihoa": "Hội họa", "trangsuc": "Trang sức", "doluuniem": "Đồ lưu niệm", "doco": "Đồ cổ"}
        type_room = category[typeroom]
        x = [x for x in db.item.find({"_id": ObjectId(str(app.primaryItemId[app.indexRoom[typeroom]]))}, {"price_max": True, "id_bidder": True})][0]
        try:
            flagTop1Bidder = 1 if x["id_bidder"] == session["id"] else 0
        except:
            flagTop1Bidder = 0
        return appFlask.response_class(json.dumps({"status": "SUC", "timeRemaining": room.checkTimeRemaining(typeroom), "price_max": x["price_max"], "flagTop1Bidder": flagTop1Bidder}),mimetype='application/json')
    except:
        return appFlask.response_class(json.dumps({"status": "ERR"}),mimetype='application/json')
    