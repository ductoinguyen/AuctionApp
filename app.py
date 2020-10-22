from flask import Flask, request, jsonify, render_template
import os, json, threading, time
import pandas as pd
import numpy as np

# app = Flask(__name__)
TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')

# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/getReview/<int:hotel_id>", methods=["POST"])
def getReview(hotel_id):
    data = []
    # df = query.getReviews(hotel_id)
    df = None
    for index, row in df.iterrows(): 
        data.append({
            "time": row[0],
            "title": row[1],
            "content": row[2],
            "score":row[3]
        })
    return app.response_class(json.dumps(data),mimetype='application/json')

@app.route("/", methods=["GET"])
def home():
    return render_template('render/home.html')

if __name__ == "__main__":
    app.run(debug=True)
