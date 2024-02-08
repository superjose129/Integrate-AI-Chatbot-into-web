
# 2.---Develop web-app using Flask and integrate model---#
import os

# from flask_socketio import SocketIO
import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
# import secrets

# socketio = SocketIO()

app = Flask(__name__)
# app.config["SECRET_KEY"] = secrets.token_urlsafe(32)
model = pickle.load(open('model.pkl','rb'))
# print(model)
# @app.route('/')
# def home():
#     return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    seed = data['seed']
    num_words = data['numWords']
    generate_text = data['generatedText']

    final_features = [np.array([seed, num_words, generate_text])]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2) 
    print(output)
    return jsonify({'output':output})
    # return render_template('index.html', prediction_text='CO2    Emission of the vehicle is :{}'.format(output))

if __name__ == "__main__":
    # from waitress import serve
    # serve(app, host="localhost", port=3000)
    app.run(port=3000)