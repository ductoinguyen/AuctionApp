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
        return (x['_id'], "auctioneer")
    result = (db.bidder.find({"username": username, "password": password}, {"_id": True, "name": True}))
    for x in result:
        break
    if len(x) > 0:
        return (x['_id'], "bidder")
    result = (db.admin.find({"username": username, "password": password}, {"_id": True, "name": True}))
    for x in result:
        break
    if len(x) > 0:
        return (x['_id'], "admin")
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

def bid():
    appFlask = app.app
    db = app.db
    try:
        id_bidder = session["id"]
        username = session["username"]
        price = request.form['price']
        id_item = request.form['id_item']
        (max_price_current, item_name, item_category) = [(x["price_max"], x["name"], x["category"]) for x in db.item.find({"_id": ObjectId(id_item)}, {"price_max": True, "name": True, "category": True})][0]
        if price <= max_price_current:
            return appFlask.response_class(json.dumps({"result": "Thất bại"}),mimetype='application/json')
        accountBalance = [x["accountBalance"] for x in db.bidder.find({"_id": ObjectId(id_bidder)}, {"accountBalance": True})][0]
        if accountBalance < price:
            return appFlask.response_class(json.dumps({"result": "Số dư tài khoản không đủ"}),mimetype='application/json')
        db.item.update({"_id": ObjectId(id_item)}, {"$set": {"price_max": price, "id_bidder": id_bidder}})
        db.bidder_history.insert({"id_bidder": id_bidder, "status": "auction", "id_item": id_item, "item_name": item_name, "item_category": item_category, "price": price})
        room.updateTimeRemaining(item_category)
        return appFlask.response_class(json.dumps({"result": "Thành công"}),mimetype='application/json')
    except:
        return appFlask.response_class(json.dumps({"result": "Thất bại"}),mimetype='application/json')

def getPrimaryItemInRoom(typeroom):
    appFlask = app.app
    db = app.db
    try:
        typeroom = typeroom.strip()
        (currentDate, currentHour) = room.getTime()
        category = {"thoitrang": "Thời trang", "hoihoa": "Hội họa", "trangsuc": "Trang sức", "doluuniem": "Đồ lưu niệm", "doco": "Đồ cổ"}
        type_room = category[typeroom]
        x = [x for x in db.item.find({"open_bid": currentDate, "status": "ready to auction", "category": type_room, "index_session": currentHour}).limit(1)][0]
        app.primaryItemId[app.indexRoom[type_room]] = str(x["_id"])
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
        print(currentDate, currentHour)
        category = {"thoitrang": "Thời trang", "hoihoa": "Hội họa", "trangsuc": "Trang sức", "doluuniem": "Đồ lưu niệm", "doco": "Đồ cổ"}
        type_room = category[typeroom]
        result = db.item.find({"open_bid": currentDate, "status": "ready to auction", "category": type_room, "index_session": currentHour}, {"_id": True, "name": True, "image": True}).skip(1)
        data = [{"status": "SUC"}]
        for x in result:
            data.append({
                "id_item": str(x["_id"]),
                "name": x["name"],
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

def getPricemaxTime(loaiphong, id_item):
    id_item = id_item.strip()
    appFlask = app.app
    return appFlask.response_class(json.dumps([{"timeremaning": room.checkTimeRemaining(loaiphong)}]),mimetype='application/json')