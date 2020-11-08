from flask import Flask, request, jsonify, render_template, session, redirect, url_for, escape
import app, json
from controllers import db_controller
from bson.objectid import ObjectId
from datetime import datetime

def getNameAccount():
    appFlask = app.app
    try:
        return appFlask.response_class(json.dumps({"name_account": session["name_account"]}), mimetype='application/json')
    except:
        return appFlask.response_class(json.dumps({"name_account": "Tài khoản"}), mimetype='application/json')

def getIdAuctioneer():
    appFlask = app.app
    db = app.db
    x = [x for x in db.auctioneer.find({"_id": ObjectId(str(session["id"]))})][0]
    return appFlask.response_class(json.dumps({"id_auctioneer": str(session["id"]), "name": x["name"], "address": x["address"], "birthday": str(x["birthday"]).split(" ")[0], "accountBalance": x["accountBalance"], "phoneNumber": x["phoneNumber"]}), mimetype='application/json')

def getInfoBidder():
    appFlask = app.app
    db = app.db
    x = [x for x in db.bidder.find({"_id": ObjectId(str(session["id"]))})][0]
    return appFlask.response_class(json.dumps({"name": x["name"], "address": x["address"], "birthday": str(x["birthday"]).split(" ")[0], "accountBalance": x["accountBalance"], "phoneNumber": x["phoneNumber"]}), mimetype='application/json')   

def setInfoBidder():
    appFlask = app.app
    db = app.db
    id_bidder = session["id"]
    try:
        nameAccount = request.form['nameAccount']
        address = request.form['address']
        birthday = request.form['birthday']
        phoneNumber = request.form['phoneNumber']
    except:
        nameAccount = request.get_json()['nameAccount']
        address = request.get_json()['address']
        birthday = request.get_json()['birthday']
        phoneNumber = request.get_json()['phoneNumber']     
    db.bidder.update({"_id": ObjectId(id_bidder)}, {"$set": {"name": nameAccount, "address": address, "birthday": birthday, "phoneNumber": phoneNumber}})
    session["name_account"] = nameAccount
    return appFlask.response_class(json.dumps({"result": "success"}), mimetype='application/json') 

def getAllHistoryAuction():
    appFlask = app.app
    db = app.db
    id_bidder = session["id"]
    result = [x for x in db.bidder_history.find({"id_bidder": (id_bidder), "status": "auction"})] 
    # print(result, id_bidder)
    (price_start, id_bidder_max, id_item_before, open_bid, status, image, price_max) = ("", "", "", "", "", "", "")
    data = []
    for i in range(len(result) - 1, 0, -1):
        try:
            item = result[i]
            (id_item, price, item_name) = (item["id_item"], item["price"], item["item_name"])
            if id_item_before != id_item:
                (price_start, id_bidder_max, id_item_before, open_bid, status, image, price_max) = [(x["price_start"], str(x["id_bidder"]), str(x["_id"]), str(x["open_bid"]).split(" ")[0], x["status"], x["image"], x["price_max"]) for x in db.item.find({"_id": ObjectId(id_item)})][0]
            if id_bidder == id_bidder_max:
                if status == "paid":
                    if price == price_max:
                        result_status = "Thành công"
                    else:
                        result_status = "Thất bại"
                else:
                    result_status = "Đang diễn ra"
            else:
                result_status = "Thất bại"
            data.append({
                "id_item": id_item,
                "item_name": item["item_name"],
                "price_start": price_start,
                "price": item["price"],
                "open_bid": open_bid,
                "status": result_status,
                "image": image
            })
        except:
            continue
    return appFlask.response_class(json.dumps(data), mimetype='application/json') 

def submitSignup():
    appFlask = app.app
    db = app.db
    try:
        username = request.form['username']
        password = request.form['password']
        nameAccount = request.form['nameAccount']
        address = request.form['address']
        birthday = request.form['birthday']
        phoneNumber = request.form['phoneNumber']
    except:
        username = request.get_json()['username']
        password = request.get_json()['password']
        nameAccount = request.get_json()['nameAccount']
        address = request.get_json()['address']
        birthday = request.get_json()['birthday']
        phoneNumber = request.get_json()['phoneNumber']   
    createDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    db.bidder.insert({"username": username, "password": password, "name": nameAccount, "address": address, "birthday": birthday, "accountBalance": 0, "createDate": createDate})
    session['username'] = username
    session['password'] = password
    session['type_account'] = "bidder"
    session['name_account'] = nameAccount
    session['id'] = [str(x["_id"]) for x in db.bidder.find({"username": username})][0]
    return appFlask.response_class(json.dumps({"result": "Thành công", "type_account" : session['type_account']}), mimetype='application/json')


def deleteAccount(username):
    appFlask = app.app
    db = app.db
    db.bidder.remove({"username": username})
    db.auctioneer.remove({"username": username})
    return appFlask.response_class(json.dumps({"result": "ok"}), mimetype='application/json')