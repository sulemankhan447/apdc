from flask import Flask, render_template,request,flash, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt
import pandas as pd
import math


app = Flask(__name__)

app.config['SECRET_KEY'] = "a95ec5d5d69e5e75d869feb78c35d2e15090ae5e2259a5b6"
app.config["MONGO_URI"] = "mongodb://localhost:27017/apdc"

mongo = PyMongo(app)

def read_csv(category):
    startup_dict = {}
    # csv = open("START.csv","r","encoding = utf-8")
    dataset = pd.read_csv("START.csv")
    name = (dataset.iloc[:, 0:1]).values.tolist()
    logo = (dataset.iloc[:, 6:7]).values.tolist()
    status = (dataset.iloc[:, 1:2]).values.tolist()
    fund = (dataset.iloc[:, 8:9]).values.tolist()
    website_link = (dataset.iloc[:, 9:10]).values.tolist()
    founded = (dataset.iloc[:, 2:3]).values.tolist()
    categories = (dataset.iloc[:, 4:5]).values.tolist()
    
    # print(categories)
    categories = sum(categories, [])
    name = sum(name, [])
    logo = sum(logo, [])
    status = sum(status, [])
    fund = sum(fund,[])
    website_link = sum(website_link, [])
    founded = sum(founded, [])
    startup_list = []
    startup_key = ''
    startup_name = []
    startup_logo = []
    startup_foundedat =[]
    startup_website = []
    startup_status = []

    for j in range(len(categories)-1):
        if (category) in str(categories[j]):
            startup_key = name[j]
            startup_list.append(logo[j])
            startup_list.append(founded[j])
            startup_list.append(website_link[j])
            startup_list.append(status[j])

            startup_dict[startup_key] = startup_list
            startup_list = []
            

    # print(startup_name, startup_foundedat,)

    return startup_dict
@app.route('/')
def index():
    return render_template('index.html', name = False)

@app.route('/startup_comp', methods = ['GET', 'POST'])
def startup_comparator():
    if request.method == "POST":
        startup = mongo.db.startup
        
        p_type = request.form['p_type']
        
        startup_dict = read_csv(p_type)
        
        startup.insert({'products':[ {'product_name' : request.form['p_name'], 'product_type' : request.form['p_type'], 'usp' : request.form['usp']} ] })
        return render_template('startup_compare.html', dic = startup_dict ,name = True)
    else:
        return render_template('startup_compare.html' ,name = False)

@app.route('/ratio',methods=['GET','POST'])
def cac_ratio():
    if request.method == 'POST':
        tot_acqui = int(request.form['arc'])
        noCust =int (request.form['acl'])
        avgorder = int(request.form['avgorder'])
        noorder = int(request.form['nooforder'])
        uniqueCust = int(request.form['uniqueCust'])
        pf =  int(noorder/uniqueCust)
        pro = int(request.form['profit'])
        cac = int(tot_acqui / noCust)
        clv = int(avgorder * pf * uniqueCust)
        rat = float(cac / clv)
        ratio = math.ceil(rat)
        print('CAC : '+str(cac)+'CLV : '+str(clv)+' Ratio of CAC:CLV : '+str(ratio))
    return render_template('ratio.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['name']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['name'], 'password' : hashpass,'email' :request.form['email']})
            session['name'] = request.form['name']
            return redirect('/')
        return 'That username already exists!'

    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def getLogin():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name' : request.form['username']})

        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
               session['username'] = request.form['username']
        return redirect('/')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)