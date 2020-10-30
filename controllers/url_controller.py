from flask import Flask, request, jsonify, session, redirect, url_for, escape, render_template
import os, json
import app
from bson.objectid import ObjectId
import controllers.db_controller as db_controller

def homeController():
    # neu chua dang nhap => chuyen den trang dang nhap
    # neu da dang nhap roi thi hien thi binh thuong
    if 'username' not in session:
        return redirect('dang-nhap')
    return render_template('render/home.html')

def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect('/')

def submitLogin():
    appFlask = app.app
    try: 
        username = request.form['username']
        password = request.form['password']
    except:
        data = {"result": "Đăng nhập lại"}
        return appFlask.response_class(json.dumps(data),mimetype='application/json')
    # print(username + " " + password)
    checkLogin = db_controller.checkLogin(app.db, username, password)
    if checkLogin == -1:
        return appFlask.response_class(json.dumps({"result": "Kiểm tra lại username và password"}), mimetype='application/json')
    session['username'] = username
    session['password'] = password
    session['id'] = str(checkLogin[0])
    session['type_account'] = checkLogin[1]
    return appFlask.response_class(json.dumps({"result": "Thành công"}), mimetype='application/json')

