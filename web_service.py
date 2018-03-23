from flask import Flask, request, jsonify
from main import create_user, add_heart_rate, print_user, get_hr_user
from main import calculate_hr
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

@app.route("/api/heart_rate/<email>", methods=["GET"])
def get_all_hr(email):
    """returns all heart rate measurements for the user"""
    try:
        get_hr_user(email)
        return jsonify("heart rate responses:", user.heart_rate)
    except:
        return "User not found"

@app.route("/api/heart_rate/average/<email>", methods=["GET"])
def get_avg_hr(email):
    """returns the average heart rate of all measurements of a user
    """
    try:
        avg_hr = calculate_hr(email)
        print(avg_hr)
        return jsonify("average heart rate is",  avg_hr)
    except:
        return "Try again, user email not found"

@app.route("/api/heart_rate/interval_average", methods=["POST"])
def get_avg_hr_interval():
    r = request.get_json()
    interval = r["time"]
    print(interval)
    email = r["user_email"]
    print(email)
    df = user.heart_rate
    index = df.truncate(before=interval)
    print(index)
    return index
   # except:
      #  return "time is outside of range, values not found"

if __name__ =="__main__":
    app.run(host="127.0.0.1")


