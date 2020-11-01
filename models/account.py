from flask import Flask, request, jsonify, render_template, session, redirect, url_for, escape
import app, json

def getNameAccount():
    appFlask = app.app
    return appFlask.response_class(json.dumps({"name_account": session["name_account"]}), mimetype='application/json')