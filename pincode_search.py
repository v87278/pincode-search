from flask import Flask, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Get MongoDB configuration from environment variables

print(os.getenv('MONGO_USERNAME'), os.getenv('MONGO_PASSWORD'), os.getenv('MONGO_HOST'), os.getenv('MONGO_PORT'))

MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')
DATABASE_NAME = os.getenv('DATABASE_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

# Construct MongoDB URI with properly escaped username and password
MONGO_URI = f'mongodb://{quote_plus(MONGO_USERNAME)}:{quote_plus(MONGO_PASSWORD)}@{MONGO_HOST}:{MONGO_PORT}/'

# Connect to MongoDB using configuration from environment variables
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

@app.route('/get_data', methods=['GET'])
def get_data():
    pincode = request.args.get('pincode')

    if pincode:
        # Query MongoDB collection for pincode
        pincode_data = collection.find_one({'pincode': pincode}, {'_id': 0})

        if pincode_data:
            return jsonify(pincode_data)
        else:
            return jsonify({'error': 'Pincode not found'}), 404
    else:
        return jsonify({'error': 'Pincode parameter is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
