

# Flask imports
from flask import Flask, render_template, request, redirect, url_for, send_file, session


# unwanted pythton scripts
from additional import * 

# for creating and deleting the file import os, shutil, tempfile
import os, shutil, tempfile

# for naming the created file
import time

app = Flask(__name__)
app.secret_key = " not 'soo secret' key"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        file = request.files['file_name']
        file_contents = file.readlines()
        file_contents = to_utf8(file_contents)
        splited_name = file.filename.rsplit('.')
        session['file_name'] = splited_name[0] + "." + str(time.time()) + '.txt'
                
        if request.form['crypt'] == "encrypt": 
            with open("downloads/" + session['file_name'], "w") as f:
                f.writelines(encrypted_text(file_contents))
                
        if request.form['crypt'] == "decrypt":
            with open("downloads/" + session['file_name'], "w") as f:
                    f.writelines(decrypted_text(file_contents))               
                
        return redirect(url_for('download_file'))
    return render_template('index.html')

@app.route('/download/file')
def download_file():
    # Read the created file into a temporary file and delete the file to save space
    cache = tempfile.NamedTemporaryFile()
    with open("downloads/" + session['file_name'], 'rb') as fp:
        shutil.copyfileobj(fp, cache)
        cache.flush()
    cache.seek(0)
    os.remove("downloads/" + session['file_name'])
    return send_file(cache, as_attachment=True, attachment_filename=session['file_name']) 



if __name__ == '__main__':
    app.run(debug=True)
