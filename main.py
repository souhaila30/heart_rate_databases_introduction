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
    user = models.User.objects.raw({"_id":email}).first()
    all_hr = user.heart_rate
    return all_hr

def calculate_hr(all_hr):
    """calculate the average heart rate for a user

    :param email: email of user
    """
    avg_hr = np.mean(all_hr)
    return avg_hr

def find_time(email, interval):
    """finds the heart rates within a time interval specified by the user

    :param email: email of user
    :param interval: start of time interval
    """

    user = models.User.objects.raw({"_id":email}).first()
    formatted_interval = dateutil.parser.parse(interval)
    print(type(formatted_interval))
    hr = user.heart_rate
    time = user.heart_rate_times
    print(hr)
    print(time)
    time_diff = np.abs([i - interval for i in time])
    print(time_diff.argmin(0))
#    print(new_hr)
    return "No errors yet"

def return_age(email):
    """returns the age of the user
    """
    user = models.User.objects.raw({"_id":email}).first()
    age = np.max(user.age)
    return age

def check_tachycardia(age, avg_hr):
    """checks the average heart rate and returns if the user has tachycardia
    :param email: email of user
    :param age: age of user
    :param avg_hr: average heart rate of the user
    """
    #user = models.User.objects.raw({"_id":email}).first()
    #age = np.max(user.age)
    #print(age)
    #avg_hr = calculate_hr(email)
    #print(avg_hr)

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

