
import requests
import os
from flask import Flask, request, redirect, url_for, send_from_directory,render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/tmp/flask-upload-test/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print 'no file'
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print 'no filename'
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
#    return '''
#        <!doctype html>
#        <title>Upload Image</title>
#        <h1>Upload new File</h1>
#        <form action="" method=post enctype=multipart/form-data>
#        <p><input type=file name=file>
#        <input type=submit value=Upload>
#        </form>
#        '''
    return render_template('upload.html')

@app.route('/')
def main():
    return '''
        .uhertldgjatek
        '''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == "__main__":
    app.run(debug=True)
    api_key = 'acc_5c6d4027d0c5727'
    api_secret = '1358efce01368542fed83c3f9c111646'
    image_url = filename




    response = requests.get('https://api.imagga.com/v1/tagging?url=%s' % image_url,auth=(api_key, api_secret))
    print response.json()
#return '''
#    <!doctype html>
#    <script>
#    document.write("<p style='color: aliceblue; display: inline'> "+response.tags+"<\p>")
#    </script>
#    '''




