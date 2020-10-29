import pymongo
from pymongo import MongoClient
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process 
import os
import threading
from bson.objectid import ObjectId

# import app

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


# db = getDB()
# print(checkLogin(db, "trungvuthanh", "12345678"))
# r = db.bidder.find({"_id": ObjectId('5f8b09b5324188afd7be2ac7')})
# for x in r:
#     print(x['name'])
# print()

# def testcheckLogin(db, username, password):
#     try:
#         result = (db.watermelishCollection.find({"username": username, "password": password}, {"_id": True}))
#         for x in result:
#             break
#         return (str(x['_id']))
#     except:
#         return -1

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

def signup(db, username, password, name):
    try: 
        # db = getDB()
        if checkAccount(db, username) == "yes":
            return "thất bại"
        db.watermelishCollection.insert({"username": username, "password": password, "name": name})
        return "thành công"
    except:
        return "thất bại"

    
def editAccount(db, new_password, newname):
    try:
        if checkLogin(db, username, old_password) == -1:
            return "Sai mật khẩu"
        db.watermelishCollection.update({"username": username}, {"$set": {"password": new_password, "name": name}})
        return "Thành công"
    except:
        return "Thất bại"

# print(searchWord("nhom13", "interlet"))

# db = getDB()
# print(getTarget(db, "nhom13"))