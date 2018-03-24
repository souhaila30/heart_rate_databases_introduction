from flask import Flask, request, jsonify
from main import create_user, add_heart_rate, print_user, get_hr_user
from main import calculate_hr, find_hr_interval, check_tachycardia, return_age
from main import get_user
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
        all_hr = get_hr_user(email)
        return jsonify(calculate_hr(all_hr)), 200
    except:
        return "Try again, user email not found", 400

@app.route("/api/heart_rate/interval_average", methods=["POST"])
def get_avg_hr_interval():
    try:
        r = request.get_json()
        interval = r["time"]
        email = r["user_email"]
        return jsonify(find_hr_interval(email, interval)), 200
    except:
        return "Error: try a different interval or email", 400

@app.route("/api/heart_rate/is_tachycardia/<email>", methods=["GET"])
def is_tachycardia(email):
    try:
        all_hr = get_hr_user(email)
        avg_hr = calculate_hr(all_hr)
        age = return_age(email)
        return jsonify(check_tachycardia(age, avg_hr)), 200
    except:
        return "Something went wrong, try again", 400

@app.route("/api/all_data/<email>", methods=["GET"])
def get_info(email):
    try:
        return jsonify(get_user(email)), 200
    except:
        return "Error, try a different email", 400

if __name__ =="__main__":
    app.run(host="127.0.0.1")


