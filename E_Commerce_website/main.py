from flask import Flask, render_template
import requests
import csv
from io import StringIO

app = Flask(__name__)

# Google Sheet CSV link
CSV_URL = "https://docs.google.com/spreadsheets/d/1e7dBXSF0WwFqfJOxs4bzEVbmXZbVrLwl4ASs4o9kCvM/pub?gid=0&single=true&output=csv"

def fetch_csv_data(url):
    response = requests.get(url)
    csv_text = response.text
    f = StringIO(csv_text)
    reader = csv.DictReader(f, delimiter=',')
    data = [row for row in reader]
    return data

@app.route('/')
def index():
    products = fetch_csv_data(CSV_URL)
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
