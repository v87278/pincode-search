from flask import Flask, jsonify, request
from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

app = Flask(__name__)

# Connect to MongoDB using configuration from config.py
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
