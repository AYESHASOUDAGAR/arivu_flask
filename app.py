from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from flask_cors import CORS
import jwt
from pymongo import MongoClient
from user import createUser, updateUser

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'asdf5tyhb23wedrft'


@app.route('/')
def hello_world():
    return 'Hello Ayesha'

@app.route('/school/reg',methods=['POST'])    #end point
def reg():
    data=request.get_json()
    result = createUser(data)
    return jsonify(result)

 
@app.route('/school/login',methods=['POST'])   #end point
def school_login():
    username = request.json.get('email')
    password = request.json.get('password')
    print(username,password)


    mongo_uri = "mongodb://localhost:27017/arivu"
    client = MongoClient(mongo_uri)
    db = client['arivu']
    collection = db['user']
    # Example: Check if the username and password are valid
    found = list(collection.find({"email":username, "password":password}))
    if (len(found) > 0):
        # Create a JWT token
        try:
            token = jwt.encode({'username': username, 'exp': datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
            print("Token : ",token)
            data = {
                "user":username,
                "token": token
            }
        except Exception as e:
            print("Error in login : ",e)
        return jsonify(data)
    else:
        return jsonify({'error': 'Invalid credentials'}), 401


@app.route("/school/add_class_video", methods=["POST"])
def addSchool_video():
    link = request.get_json()
    mongo_uri = "mongodb://localhost:27017/arivu"
    client = MongoClient(mongo_uri)
    db = client['arivu']
    collection = db['school_videos']
    data = {
        "class_name":link['class_name'],
        "sub_name":link['sub_name'],
        "school_name":link['school_name'],
        "video":link['video'],
        "pdf":link['pdf']
    }
    try:
        result = collection.find({"class_name":link["class_name"],"sub_name":link["sub_name"],"school_name":link["school_name"]})
        result = list(result)
        # {'$set': {'new_field': data['new_value']}}
        if(len(result) > 0):
           collection.update_one({'sub_name': data['sub_name']}, {'$set': data})
        collection.insert_one(data)
        return "success"
    except Exception as e:
        print("Error in add school videos : ",e)
        return "Failed"
    
@app.route("/school/get_class_video", methods=["POST"])
def getSchool_video():
    link = request.get_json()
    mongo_uri = "mongodb://localhost:27017/arivu"
    client = MongoClient(mongo_uri)
    db = client['arivu']
    collection = db['school_videos']
    try:
        result = collection.find({"class_name":link["class_name"],"sub_name":link["sub_name"],"school_name":link["school_name"]})
        result = list(result)
        print(result, type(result))

        vlink = result[0]["video"]
        print(vlink)
        return str(vlink)
    except Exception as e:
        print("Error in add school videos : ",e)
        return "Failed"
    
# main driver function
if __name__ == '__main__':
    app.run(debug=True)
