# Import dependencies
import os
import json
import collections
import flask 
from flask import Flask, jsonify, render_template, request
from flask_cors import cross_origin 

# Setup Flask
# Create an app, pass to __name__
app = Flask(__name__)

# app.config['UPLOAD_FOLDER'] = 


@app.route("/", methods=['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')    

# Set up Upload File 
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        return 'file uploaded successfully'

if __name__ == "__main__":
    app.run(debug=True)