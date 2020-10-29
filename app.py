from flask import Flask, request, jsonify, render_template, session, redirect, url_for, escape
from controller import url_controller, db_controller
import os, json, threading, time
import pandas as pd
import numpy as np

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = db_controller.getDB()

@app.route("/", methods=["GET"])
def home():
    return url_controller.homeController()

@app.route("/dang-nhap", methods=["GET"])
def renderPageLogin():
    return render_template('render/login.html')

@app.route("/submit-dang-nhap", methods=["POST"])
def login():
    return url_controller.submitLogin()


@app.route("/dang-xuat", methods=["GET"])
def logout():
    session.pop('username', None)
    return redirect(url_for('/'))


@app.route("/phong-dau-gia", methods=["GET"])
def room():
    return render_template('render/room.html')



@app.route("/dang-ky", methods=["GET"])
def signup():
    return render_template('render/signup.html')

if __name__ == "__main__":
    app.run(debug=True)
