from flask import Flask, request, jsonify
from main import create_user, add_heart_rate, print_user
import models
import numpy as np
import datetime
from pymodm import connect

connect("mongodb://localhost:27017/heart_rate_app")
app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello, world"

@app.route("/api/heart_rate", methods=['POST'])
def heart_rate():
    """
    Updates heart rate database with user input
    """

    r = request.get_json()
    email = r["user_email"]
    age = r["user_age"]
    heart_rate = r["heart_rate"]
    time = datetime.datetime.now()
    print(email,age, heart_rate)
    try:
        add_heart_rate(email, heart_rate, time)
        print("User found, responses recorded")
        return jsonify(email, heart_rate, time)
    except:
        print("user not found, a new user was created")
        create_user(email, age, heart_rate)
        return jsonify(email, age, heart_rate, time)

@app.route("/api/print_user/<user_email>", methods=["GET"])
def get_print_user(user_email):
    """print all the information associated with the user email
    """
    try:
        print_user(user_email)
        return "User responses were printed"
    except:
        return "User not found"

@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def get_all_hr(user_email):
    """returns all heart rate measurements for the user"""
    try:
        user = models.User.objects.raw({"_id":user_email}).first()
        return jsonify("heart rate responses:", user.heart_rate)
    except:
        return "User not found"

@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def get_avg_hr(user_email):
    user = models.User.objects.raw({"_id":user_email}).first()
    print(user.heart_rate)
    avg_hr = np.mean(user.heart_rate)
    print(avg_hr)
    return jsonify("average heart rate is",  avg_hr)

@app.route("/api/heart_rate/interval_average", methods=["POST"])
def get_avg_hr_interval(user_email, interval):
    user = models.User.objects.raw({"_id":user_email}).first()
    r = request.get_json()
    interval = 
    max_time = datetime.max(user.user_time)
    print(max_time)

if __name__ =="__main__":
    app.run(host="127.0.0.1")


