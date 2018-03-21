from flask import Flask, request, jsonify
from main import create_user, add_heart_rate, print_user
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
        user = models.User.objects.raw({"_id":email}).first()
        add_heart_rate(email, heart_rate, time)
        return(email, heart_rate, time)
    except:
        print("user not found, a new user was created")
        create_user(email, age, heart_rate)
        return(email, age, heart_rate, time)

@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def get_all_hr(user_email):
    """returns all heart rate measurements for the user"""
    all_hr = request.get(user_email)
    return all_hr

@app.route("/api/heart_rate/Average/<user_email>", methods=["GET"])
def get_avg_hr():
    all_hr = request.get(user_email)
    num_hr = len(all_hr)
    avg_hr = [(np.mean((all_hr[i], all_hr[i+1]))) for i in range (len(all_hr)-1)]
    return avg_hr

if __name__ =="__main__":
    app.run(host="127.0.0.1")


