from flask import Flask
from db import db
from flask_cors import CORS
from visitors import visitors_blueprint
from dashboard import dashboard_bluprint

app=Flask(__name__)
CORS(app)

# Database Config
username='root'
password=""
userpass='mysql+pymysql://' + username + ':' +password + '@'
server = '127.0.0.1'
db_name = '/walmart_visitors'

app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True

db.init_app(app)
#API End point - Route*

app.register_blueprint(visitors_blueprint)
app.register_blueprint(dashboard_bluprint)

@app.route('/')
def serverStaus():
    return 'server is up and running'

if __name__=='__main__':
    app.debug=True
    app.run()