from flask import Flask, render_template, redirect, jsonify, request, url_for
import random
import smtplib
import datetime as dt
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html",)


@app.route("/signup_page.html", methods=['GET', 'POST'])
def signup_page():
    global otp
    my_email = "codewithmrpy@gmail.com"
    password = "eaflyqlwydcznrgt"
    if request.method == "POST":
        otp = random.randint(100000, 999999)
        email = request.form['email']
        # password = request.form['password']
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"subject:Your signup OTP \n\n {otp}")
        return redirect(url_for('OTP_a', email=email, otp=otp))
    else:
        pass
    return render_template("signup_page.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=True)