from flask import Blueprint,request
from sqlalchemy.sql import text
import datetime
from db import db

visitors_blueprint=Blueprint('visitors_blueprint',__name__)

@visitors_blueprint.route('/log_visitors', methods=['POST'])
def addVistorsData():
    gender = request.form['gender']
    ageGroup = request.form['age_group']
    currentDate = datetime.datetime.today().strftime("%Y-%m-%d")
    currentTime=datetime.datetime.now().strftime("%H:%M:%S")


    sql = text('INSERT INTO visitors_log (gender,age_group,date,time) VALUES ('+str(gender)+','+str(ageGroup)+',"'+currentDate+'","'+currentTime+'")')

    db.engine.execute(sql)
    return "Data logged succesfully"