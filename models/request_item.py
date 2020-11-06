from datetime import datetime
import time
import app, json
from bson.objectid import ObjectId
from flask import Flask, request, jsonify, render_template, session, redirect, url_for, escape

def filterDate(create_date):
    difference = datetime.now() - datetime.strptime(create_date, "%d/%m/%Y")
    tupleTime = divmod(difference.days * (24*60*60) + difference.seconds, 60)
    return (tupleTime[0]*60 + tupleTime[1])/(24*60*60)
    

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
    if len(result) < 5:
        result = result[::5]
    result = [item["id"] for item in result]
    result = [{
                "id": str(x["_id"]),
                "name": x["name"],
                "content": x["content"],
                "image": x["image"],
                "price_start": x["price_start"],
                "category": x["category"]
            } for x in db.item.find({"_id": {"$in": result}})]
    return appFlask.response_class(json.dumps(result), mimetype='application/json')