from flask import Flask, request, jsonify
from main import create_user, add_heart_rate, print_user, get_hr_user
from main import calculate_hr, find_time, check_tachycardia
import models
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
    print(email,age, heart_rate, time)
    try:
        add_heart_rate(email, heart_rate, time)
        print("User found, responses recorded")
        return jsonify(email, heart_rate, time), 200
    except:
        print("user not found, a new user was created")
        create_user(email, age, heart_rate)
        return jsonify(email, age, heart_rate), 200

@app.route("/api/heart_rate/<email>", methods=["GET"])
def get_all_hr(email):
    """returns all heart rate measurements for the user"""
    try:
        return jsonify(get_hr_user(email))
    except:
        return "User not found", 400

@app.route("/api/heart_rate/average/<email>", methods=["GET"])
def get_avg_hr(email):
    """returns the average heart rate of all measurements of a user
    """
    try:
        return jsonify(calculate_hr(email)), 200
    except:
        return "Try again, user email not found", 400

@app.route("/api/heart_rate/interval_average", methods=["POST"])
def get_avg_hr_interval():
    r = request.get_json()
    interval = r["time"]
    print(interval)
    email = r["user_email"]
    print(email)
    print(find_time(email, interval))
    return "it is working well so far", 200

@app.route("/api/heart_rate/is_tachycardia/<email>", methods=["GET"])
def is_tachycardia(email):
    return jsonify(check_tachycardia(email))

if __name__ =="__main__":
    app.run(host="127.0.0.1")


