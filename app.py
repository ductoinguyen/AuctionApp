from flask import Flask, request, jsonify, render_template, session, redirect, url_for, escape
from controllers import url_controller, db_controller
import os, json, threading, time
import pandas as pd
import numpy as np
from datetime import datetime
from models import room

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = db_controller.getDB()
timeRoom = room.initTimeRoom()
indexRoom = room.createIndexRoom()
primaryItemId = ["" for _ in range(5)]

@app.route("/dang-nhap", methods=["GET"])
def renderPageLogin():
    return render_template('render/login.html')

@app.route("/submit-dang-nhap", methods=["POST"])
def login():
    return url_controller.submitLogin()

@app.route("/dang-xuat", methods=["GET"])
def logout():
    return url_controller.logout()

@app.route("/cac-phong-dau-gia", methods=["GET"])
def rooms():
    return render_template('render/category.html')

@app.route("/phong-dau-gia/<loaiphong>", methods=["GET"])
def room():
    return render_template('render/bid.html')

@app.route("/", methods=["GET"])
def home():
    return url_controller.homeController()

@app.route("/dang-ky", methods=["GET"])
def signup():
    return render_template('render/signup.html')

@app.route("/tra-gia", methods=["POST"])
def bid():
    return db_controller.bid()

@app.route("/san-pham-chinh/<loaiphong>", methods=["GET"])
def getItem(loaiphong):
    return db_controller.getPrimaryItemInRoom(loaiphong)

@app.route("/pricemax-time/<loaiphong>/<id_item>", methods=["GET"])
def getPricemaxTime(loaiphong, id_item):
    return db_controller.getPricemaxTime(loaiphong, id_item)

@app.route("/chi-tiet-san-pham/<id>", methods=["GET"])
def getDetailItem(id):
    db_controller.checkToSaveInfo(id)
    return render_template('render/detail_item.html')

@app.route("/thong-tin-san-pham", methods=["GET"])
def getInfoItem():
    return db_controller.getInfoItem(session["id_item"])

@app.route("/thong-tin-ben-a/<id>", methods=["GET"])
def getInfoAuctioneer(id):
    return db_controller.getInfoAuctioneer(id)

@app.route("/san-pham-tiep-theo/<loaiphong>", methods=["GET"])
def nextItem(loaiphong):
    return db_controller.nextItem(loaiphong)

@app.route("/lich-su-dau-gia", methods=["GET"])
def historyAuction():
    return url_controller.historyAuction()

@app.route("/test", methods=["GET"])
def test():
    # now = datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # return app.response_class(json.dumps([{"test": str(dt_string)}]),mimetype='application/json')
    return render_template('render/category.html')

if __name__ == "__main__":
    app.run(debug=True)