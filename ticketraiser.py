from flask import Flask,jsonify,request
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from werkzeug.security import safe_str_cmp


app = Flask(__name__)


app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/profile'
app.secret_key = "secretkey"
mongo = PyMongo(app)
jwt = JWTManager(app)

@app.route("/user", methods=["GET"])
def all_user():

    users = mongo.db.profile

    all_users = []

    for q in users.find():
        all_users.append({
            'name' : q['name'],
            'role' :  q['role']
        })
    return jsonify({'result': all_users})

@app.route("/user/<name>", methods=["GET"])
def one_user(name):

    users = mongo.db.profile
    
    q = users.find_one({'name': name})

    if q:
        user = {'name': q['name'],'role' : q['role']}
    else:
        return "No Result Found"

    return jsonify({'result': user})

@app.route('/add_user',methods = ["POST"])
def add_user():
    users = mongo.db.profile
    data = request.get_json(force =True)
    
    name = data['name']
    role = data['role']
    password = data['password']
    # return jsonify({"result": name})

    users_id = users.insert({'name': name, 'role': role, 'password':password})
    new_user = users.find_one_or_404({'_id': users_id})

    output = {'name': new_user['name'],'role':new_user['role'],'password':password}

    return jsonify({"result": output})

@app.route('/login',methods = ["POST"])
def login():
    users = mongo.db.profile

    name = request.get_json(force = True)['name']
    password = request.get_json(force = True)['password']
    result = ""

    q = users.find_one({'name': name})
    if password == q['password']:
        access_token = create_access_token(identity = {'name': q['name'], 'role' : q['role']})
        result = jsonify({"token":access_token})
    else:
        result = jsonify({"error":"Invalid Username and Password"})

    return result


if __name__ == "__main__":
    app.run(debug=True) 