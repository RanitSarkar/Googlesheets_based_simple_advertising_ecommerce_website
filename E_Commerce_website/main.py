from flask import Flask, render_template, redirect, jsonify, request, url_for
import datetime as dt
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=True)