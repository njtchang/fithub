from flask import Flask, abort, render_template, request, redirect, url_for, send_file
import os

app = Flask(__name__)

app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    print(request.files)
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_ext = os.path.splitext(uploaded_file.filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(f'images/{uploaded_file.filename}')
    return redirect('http://localhost:5173')

@app.route('/img/<filename>', methods=['GET'])
def send_image(filename):
    file_path = f'./images/{filename}.png'
    return send_file(file_path)

@app.route('/generate')
def generate_outfit():
    shirt_id = request.args.get('shirtId', 0)
    pants_id = request.args.get('pantsId', 0)
    # image_layering.run(shirt_id, pants_id)

if __name__ == '__main__':
    app.run(debug=True, port=5001)