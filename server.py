from flask import Flask, render_template,request
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config['SECRET_KEY'] = "a95ec5d5d69e5e75d869feb78c35d2e15090ae5e2259a5b6"
app.config["MONGO_URI"] = "mongodb://localhost:27017/apdc"
mongo = PyMongo(app)

@app.route('/', methods = ['GET', 'POST'])
def startup_comparator():
    if request.method == "POST":
        return render_template('index.html')
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)