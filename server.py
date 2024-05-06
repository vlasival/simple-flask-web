from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

FILES_FOLDER = 'files/'

@app.route('/')
def list_files():
    files = os.listdir(FILES_FOLDER)
    return render_template('files.html', files=files)

@app.route('/files/<path:filename>')
def get_file(filename):
    return send_from_directory(FILES_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

