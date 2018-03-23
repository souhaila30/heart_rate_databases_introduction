from pymodm import connect
import models
import datetime
import numpy as np

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
    """ finds an existing user in the database using their email, and print the responses recorded

    :param email: email of the user
    """

    user = models.User.objects.raw({"_id": email}).first() # Get the first user where _id=email
    print(user.email)
    print(user.heart_rate)
    print(user.heart_rate_times)

def get_hr_user(email):
    """Uses email of user to find all heart rate measurements recorded

    :param email: email of user
    """
    user = models.User.objects.raw({"_id":user_email}).first()
    print user.heart_rate
    return user.heart_rate

def calculate_hr(email):
    """calculate the average heart rate for a user

    :param email: email of user
    """
    user.heart_rate = get_hr_user(email)
    print(user.heart_rate)
    avg_hr = np.mean(user.heart_rate)
    print(avg_hr)
    return avg_hr
