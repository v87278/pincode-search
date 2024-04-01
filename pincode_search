from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

# Load data from CSV into a list of dictionaries
data = []
with open('pincode_latest.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

@app.route('/get_data', methods=['GET'])
def get_data():
    pincode = request.args.get('pincode')
    if not pincode:
        return jsonify({'error': 'Please provide a pincode parameter.'}), 400

    results = [row for row in data if row['Pincode'] == pincode]
    if not results:
        return jsonify({'error': 'No data found for the provided pincode.'}), 404

    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)
