from pymongo import MongoClient

def createUser(data):
    try:
        mongo_uri = "mongodb://localhost:27017/arivu"
        client = MongoClient(mongo_uri)
        db = client['arivu']
        collection = db['user']

        # Insert a document into the collection
        found = list(collection.find({"email":data["email"]}))
        if(len(found) > 0):
            return "Email Exist"
        else:
            result = collection.insert_one(data)
            print(result)
            return "Success"
    except Exception as e:
        print("Error in crearte user : ",e)
        return "Error"
    
def updateUser(data):
    try:
        mongo_uri = "mongodb://localhost:27017/arivu"
        client = MongoClient(mongo_uri)
        db = client['arivu']
        collection = db['user']

        # Insert a document into the collection
        result = collection.update_one(data)
        print(result)
        return "Success"
    except Exception as e:
        return "Error"
    

