from flask import Flask, render_template,request,flash
from flask_pymongo import PyMongo
# import csv
import pandas as pd


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
        if ("Media") in str(categories[j]):
            startup_key = name[j]
            startup_list.append(logo[j])
            startup_list.append(founded[j])
            startup_list.append(website_link[j])
            startup_list.append(status[j])

            startup_dict[startup_key] = startup_list
            startup_list = []
            

    # print(startup_name, startup_foundedat,)

    return startup_dict

@app.route('/', methods = ['GET', 'POST'])
def startup_comparator():
    if request.method == "POST":
        # return request.form['p_type']
        p_type = request.form['p_type']
        
        startup_dict = read_csv(p_type)
        return render_template('index.html', dic = startup_dict, show= 'block' )
    else:
        return render_template('index.html' ,name = False)
if __name__ == '__main__':
    app.run(debug=True)