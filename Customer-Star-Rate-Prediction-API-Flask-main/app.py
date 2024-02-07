import os
from main import predictrating
from flask import Flask, request, jsonify, render_template
from flask import Flask, flash, request, redirect, render_template, jsonify
from werkzeug.utils import secure_filename
app = Flask(__name__)

app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# Allowed extension you can set your own
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'  # your path may be different
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table')
def index2():
    return render_template('index.html')

@app.route('/table', methods=['POST'])
def proceed2():
    if request.method == 'POST':
        print(request.form['text'])
        text = request.form['text']
        dresults = predictrating(text)
        print(dresults)
        data = dresults
        print(data)
        return render_template('table.html', data=data)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/predictstar', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        print(request.form['text'])
        text = request.form['text']
        dresults = predictrating(text)
        print(dresults)
        return jsonify(dresults)
if __name__ == "__main__":
    app.run("0.0.0.0",port=5000, debug=True)
    #app.run(debug=True)