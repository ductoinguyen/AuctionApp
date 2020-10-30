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
import os, json, threading, time
from datetime import date

def getDB():
    MONGO_URL = os.environ.get('MONGO_URL')
    if not MONGO_URL:
        MONGO_URL = "mongodb+srv://hequantri:hequantri@cluster0.q0gxn.gcp.mongodb.net/auctionDB?retryWrites=true&w=majority";
    myclient = MongoClient(MONGO_URL)
    db = myclient["auctionDB"]
    # print('ok')
    return db

def checkLogin(db, username, password):
    result = (db.auctioneer.find({"username": username, "password": password}, {"_id": True}))
    x = []
    for x in result:
        break
    if len(x) > 0:
        return (x['_id'], "auctioneer")
    result = (db.bidder.find({"username": username, "password": password}, {"_id": True}))
    for x in result:
        break
    if len(x) > 0:
        return (x['_id'], "bidder")
    result = (db.admin.find({"username": username, "password": password}, {"_id": True}))
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
        return appFlask.response_class(json.dumps({"result": "Thành công"}),mimetype='application/json')
    except:
        return appFlask.response_class(json.dumps({"result": "Thất bại"}),mimetype='application/json')

def getAllImage(typeroom):
    typeroom = typeroom.strip()
    if typeroom == "thoitrang":
        1;
    elif typeroom == "hoihoa":
        1;
    elif typeroom == "trangsuc":
        1;
    elif typeroom == "doco":
        1;
    elif typeroom == "doluuniem":
        1;