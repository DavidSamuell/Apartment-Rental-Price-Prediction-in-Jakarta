from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    bedroom = int(request.form['bedroom'])
    apt_size = float(request.form['apt_size'])
    max_watt = int(request.form['max_watt'])
    furnish_type = request.form['furnish_type']
    kecamatan = request.form['location']

    response = jsonify({
        'estimated_price': util.get_estimated_price(bedroom, apt_size, max_watt, furnish_type, kecamatan)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
    

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()