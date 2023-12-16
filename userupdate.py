from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('')
db = client['arivu']
collection = db['users']

# Update a single document
result = collection.update_one(
    {'name': 'John'},  # Filter to find the document
    {'$set': {'email': 'newemail@example.com'}}  # New values to set
)

print(f"Modified {result.modified_count} document")