from pymodm import connect
import models
import datetime
import numpy as np
import dateutil.parser


def add_heart_rate(email, heart_rate, time):

    """function takes in user email, heart rate and time, and adds the responses to the database
    for an existing user

    :param email: user email
    :param heart_rate: user heart rate
    :param time: time of data input
    """

    user = models.User.objects.raw({"_id": email}).first() # Get the first user where _id=email
    user.heart_rate.append(heart_rate) # Append the heart_rate to the user's list of heart rates
    user.heart_rate_times.append(time) # append the current time to the user's list of heart rate times
    user.save() # save the user to the database

def create_user(email, age, heart_rate):
    """function takes in user user email, age and heart rate for a new user

    :param email: email of the user
    :param age: age of the user
    :param heart_rate: heart rate of the user
    """

    u = models.User(email, age, [], []) # create a new User instance
    u.heart_rate.append(heart_rate) # add initial heart rate
    u.heart_rate_times.append(datetime.datetime.now()) # add initial heart rate time
    u.save() # save the user to the database

def print_user(email):
    """
    Appends a heart_rate measurement at a specified time to the user specified by
    email. It is assumed that the user specified by email exists already.
    :param email: str email of the user
    :param heart_rate: number heart_rate measurement of the user
    :param time: the datetime of the heart_rate measurement
    """
    user = models.User.objects.raw({"_id": email}).first()  # Get the first user where _id=email
    user.heart_rate.append(heart_rate)  # Append the heart_rate to the user's list of heart rates
    user.heart_rate_times.append(time)  # append the current time to the user's list of heart rate times
    user.save()  # save the user to the database


def get_hr_user(email):
    """Uses email of user to find all heart rate measurements recorded

    :param email: email of user
    """
    try:
        user = models.User.objects.raw({"_id":email}).first()
        all_hr = user.heart_rate
        return all_hr
    except:
        return "User not found"

def calculate_hr(all_hr):
    """calculate the average heart rate for a user

    :param email: email of user
    """
    try:
        avg_hr = np.mean(all_hr)
        return avg_hr
    except:
        return "Heart rate measurements not found"

def find_hr_interval(email, interval):
    """finds the heart rates within a time interval specified by the user

    :param email: email of user
    :param interval: start of time interval
    """
    try:
        user = models.User.objects.raw({"_id":email}).first()
        formatted_interval = dateutil.parser.parse(interval)
        heart_rate_total = 0
        heart_rate_count = 0

        for index,heart_rate in enumerate(user.heart_rate):
            heart_rate_time = user.heart_rate_times[index]
            print("index" + str(index))
            print("heart_rate" + str(heart_rate))
            print("heart_rate_time" + str(heart_rate_time))
            if heart_rate_time >= formatted_interval:
                heart_rate_total += heart_rate
                heart_rate_count += 1
                print("heart rate total" + str(heart_rate_total))

         heart_rate_avg = heart_rate_total / heart_rate_count
         print('heart rate average:', str(heart_rate_avg))
         return heart_rate_avg
    except:
        return "Something went wrong, try a different time interval"

def return_age(email):
    """returns the age of the user
    """
    try:
        user = models.User.objects.raw({"_id":email}).first()
        age = np.max(user.age)
        return age
    except:
        return "User not found"

def check_tachycardia(age, avg_hr):
    """checks the average heart rate and returns if the user has tachycardia
    :param email: email of user
    :param age: age of user
    :param avg_hr: average heart rate of the user
    """

    if age>=1 and age<=2 and avg_hr>=151:
        return "Tachycardia: True"
    elif age>=3 and age<=4 and avg_hr>137:
        return "Tachycardia: True"
    elif age>=5 and age<=7 and avg_hr>133:
        return "Tachycardia: True"
    elif age>=8 and age<=11 and avg_hr>142:
        return "Tachycardia: True"
    elif age>=12 and age<=15 and avg_hr>119:
        return "Tachycardia: True"
    elif age>15 and avg_hr>100:
        return "Tachycardia: True"
    else:
        return "Tachycardia: False"

def get_user(email):
    """Returns all responses for all attribtues for the specified user
    :param email: email of user
    :return age: age of user
    :return heart_rate: all heart rate measurements
    :return heart_rate_times: time when the heart rates were recorded

    """
    try:
        user = models.User.objects.raw({"_id":email}).first()
        age = user.age
        time = user.heart_rate_times
        hr = user.heart_rate
        return email, age, time, hr
    except:
        return "User not found"

