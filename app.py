# Import dependencies
import os
import json
import collections
import librosa
import flask 
from flask import Flask, jsonify, render_template, request
from flask_cors import cross_origin 
from werkzeug import secure_filename


# Setup Flask
# Create an app, pass to __name__
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

app.config['UPLOAD_FOLDER'] = 'uploads'

svc_model.sav


@app.route("/", methods=['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')    

# Set up Upload File 
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

data = pd.read_csv('data.csv')

    data = data.drop(['filename'],axis=1)


@app.route('/predict/<file_name>', methods=['POST'])
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
    

    # from dataframe create train_test_split

    # run model.predict

    # return results


    return render_template('index.html', )


if __name__ == "__main__":
    app.run(debug=True)