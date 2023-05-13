from flask import Blueprint,request,jsonify
from sqlalchemy.sql import text
import datetime
from db import db

dashboard_bluprint = Blueprint('dashboard_blueprint',__name__)

#todays's visitors

@dashboard_bluprint.route('/today-visitors')
def todayVisitors():

    currentDate = datetime.datetime.today().strftime("%Y-%m-%d")

    sqlTodayVisitors= text('SELECT COUNT(*) AS todays_visitors FROM visitors_log WHERE date="'+currentDate+'"')
    resultDate = db.engine.execute(sqlTodayVisitors)
    rawData=resultDate.fetchall()

    jsonData = jsonify([dict(row) for row in rawData])
    return jsonData

@dashboard_bluprint.route('/overal-visitors')
def overalVisitors():
    sqlOVisitors= text('SELECT COUNT(*) AS overal_visitors FROM visitors_log ')
    resultDate = db.engine.execute(sqlOVisitors)
    rawData=resultDate.fetchall()

    jsonData = jsonify([dict(row) for row in rawData])
    return jsonData

# male vistors

@dashboard_bluprint.route('/male-visitors')
def maleVisitors():
    sqlOVisitors= text('SELECT COUNT(*) AS male_visitors FROM visitors_log WHERE gender=1 ')
    resultDate = db.engine.execute(sqlOVisitors)
    rawData=resultDate.fetchall()

    jsonData = jsonify([dict(row) for row in rawData])
    return jsonData

# female-visitors

@dashboard_bluprint.route('/female-visitors')
def femaleVisitors():
    sqlOVisitors= text('SELECT COUNT(*) AS female_visitors FROM visitors_log WHERE gender=2 ')
    resultDate = db.engine.execute(sqlOVisitors)
    rawData=resultDate.fetchall()

    jsonData = jsonify([dict(row) for row in rawData])
    return jsonData






@dashboard_bluprint.route('/table-data')
def tableData():

    currentDate = datetime.datetime.today().strftime("%Y-%m-%d")

    for a in range(1,6):

        txtlable=''
        x=''
        if a==1:
            txtlable = 'Kids'
        elif a == 2:
            txtlable = 'Teenagers'
        elif a==3:
            txtlable = 'Youngsters'
        elif a==4:
            txtlable = 'Adults'
        elif a==5:
            txtlable = 'Senior Citizen'
    
        for g in range(1,3): #g=gender
               #todays visitors
            sqltodayVisitors=text('SELECT COUNT(*) AS Today_visitors FROM visitors_log WHERE date="'+currentDate+'" AND gender='+str(g)+' AND age_group='+str(a)+'')
            resultData=db.engine.execute(sqltodayVisitors)
            rawData=resultData.fetchall()
            ageGroupGenderToday=rawData[0].Today_visitors


            #overral visitors
            sqloverralVisitors=text('SELECT COUNT(*) AS overral_visitors FROM visitors_log WHERE gender='+str(g)+' AND age_group='+str(a)+'')
            resultData=db.engine.execute(sqloverralVisitors)
            rawOData=resultData.fetchall()
            ageGroupGenderOverral=rawOData[0].overral_visitors

            gText=''
            if g==1:
                gText='Male'
            elif g==2:
                gText='Female'

            x+='{"gender":"'+gText+'","age_group":"'+txtlable+'","Today_visitors":"'+str(ageGroupGenderToday)+'","overral_visitors":"'+str(ageGroupGenderOverral)+'"},'
               #end of the inner for loop
        #end of outer for loop
        x=x[:-1]
        jsonData='['+x+']'
        return jsonData

@dashboard_bluprint.route('/graph-data')
def graphdata():
    x=''
    for m in range(1,13):
        sqlMonthData=text('SELECT COUNT(*) AS monthly_visitors FROM visitors_log WHERE MONTH(date)="'+str(m)+'"')
        resultdata=db.engine.execute(sqlMonthData)
        rawData=resultdata.fetchall()
        totalMothlyVisitors =rawData[0].monthly_visitors
        x+='{"month":"'+str(totalMothlyVisitors)+'"},'
    x=x[:-1]

    jsonData='['+x+']'
    return jsonData