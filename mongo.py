from pymongo import MongoClient

# Replace these with your MongoDB connection details
mongo_uri = "mongodb://localhost:27017/arivu"
client = MongoClient(mongo_uri)

# Access a specific database
db = client['arivu']

# Access a specific collection within the database
collection = db['user']

# Insert a document into the collection
document = {'name': 'John Doe', 'age': 30, 'email': 'john.doe@example.com'}
result = collection.insert_one(document)
print(result)