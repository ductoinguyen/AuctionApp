from flask import Flask, request, jsonify, render_template, session, redirect, url_for, escape
import app, json

def getNameAccount():
    appFlask = app.app
    try:
        return appFlask.response_class(json.dumps({"name_account": session["name_account"]}), mimetype='application/json')
    except:
        return appFlask.response_class(json.dumps({"name_account": "Tài khoản"}), mimetype='application/json')