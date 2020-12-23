# Import dependencies
import os
import json
import collections
import librosa
import flask 
from flask import Flask, jsonify, render_template, request
from flask_cors import cross_origin 
# from werkzeug import secure_filename
import pickle
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

# Setup Flask
# Create an app, pass to __name__
app = Flask(__name__)

# Create path to models
model = pickle.load(open('svpickle_model.pkl', 'rb'))

app.config['UPLOAD_FOLDER'] = 'uploads'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')

# # Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# svc_model.sav

# Flask route for the root/index page
@app.route("/", methods=['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')    

# Set up Upload File 
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        return 'file uploaded successfully'

@app.route('/predict/<file_name>', methods=['POST'])
# from Jupyter Notebook features
def predict(file_name=None):
    y, sr = librosa.load(f'uploads/{file_name}', mono=True, duration=30)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    rmse = librosa.feature.rms(y=y)

# create the dataframe
    df = pd.DataFrame(data= [chroma_stft, spec_cent, spec_bw, rolloff, zcr, mfcc, rmse], columns= [['chroma_stft','spec_cent', 'spec_bw', 'rolloff', 'zcr', 'mfcc', 'rmse']])

# from dataframe create train_test_split
# DON'T NEED

# run model.predict
    df_predicted= model.predict(df)
# return results
    return jsonify(df_predicted)

if __name__ == "__main__":
    app.run(debug=True)