from flask import Flask, request, jsonify, render_template, session, redirect, url_for, escape
import app, json
from bson.objectid import ObjectId

def getNameAccount():
    appFlask = app.app
    try:
        return appFlask.response_class(json.dumps({"name_account": session["name_account"]}), mimetype='application/json')
    except:
        return appFlask.response_class(json.dumps({"name_account": "Tài khoản"}), mimetype='application/json')
    
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
    