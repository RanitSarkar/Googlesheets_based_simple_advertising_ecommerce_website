from flask import Flask, render_template, redirect, jsonify, request, url_for
import datetime as dt
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
