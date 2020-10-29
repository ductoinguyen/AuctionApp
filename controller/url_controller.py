from flask import Flask, request, jsonify, session, redirect, url_for, escape, render_template
import os, json
import app
import model.account.admin as admin
import controller.db_controller as db_controller

def homeController():
    # neu chua dang nhap => chuyen den trang dang nhap
    # neu da dang nhap roi thi hien thi binh thuong
    if 'username' not in session:
        return render_template('render/login.html')
    return render_template('render/home.html')

def submitLogin():
    appFlask = app.app
    try: 
        username = request.form['username']
        password = request.form['password']
    except:
        data = {"result": "Đăng nhập lại"}
        return appFlask.response_class(json.dumps(data),mimetype='application/json')
    print(username + " " + password)
    checkLogin = db_controller.checkLogin(app.db, username, password)
    if checkLogin == -1:
        return appFlask.response_class(json.dumps({"result": "Kiểm tra lại username và password"}), mimetype='application/json')
    session['username'] = username
    session['password'] = password
    session['id'] = str(checkLogin[0])
    session['type_account'] = checkLogin[1]
    return appFlask.response_class(json.dumps({"result": "Thành công", "type_account": session['id']}), mimetype='application/json')

def loginController():
    appFlask = app.app
    try: 
        username = request.form['username']
        password = request.form['password']
    except:
        data = {"result": "Đăng nhập lại"}
        return appFlask.response_class(json.dumps(data),mimetype='application/json')
    ad = admin.Admin('a', 'b')
    data = [{"result": ad.printInfo(), "username": username}]
    return appFlask.response_class(json.dumps(data),mimetype='application/json')
    
    return render_template('render/login.html')