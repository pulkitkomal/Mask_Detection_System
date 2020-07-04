from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from model import frames
from config import PATH
import os
import time

app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/results', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        f = request.files['file']
        file = f.filename.replace('.', "-").replace(' ', '-').replace('(','-').replace(')','-')
        save_file = f.filename.replace(' ', '-').replace('(','-').replace(')','-')
        try:
            f.save(secure_filename(save_file))
        except:
            return render_template(
            'error.html', error='No file selected')
        time_ = frames.detect_wihout_mask(PATH+'/{}'.format(save_file), save_file)
        # time_ = 'testing'
        # time.sleep(10)
        dir_ = PATH+'/static/{}/output'.format(file)
        list_dir = os.listdir(dir_)
        zip_dir = '/static/zips/{}.zip'.format(file)
        os.remove(save_file)
        return render_template(
            'results.html', results=list_dir, time=time_, zip_dir=zip_dir, file=file
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)