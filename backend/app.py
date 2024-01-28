from flask import Flask, abort, render_template, request, redirect, url_for, send_file
import os
from multiprocessing import Value


shirt_counter = Value('i', 0)
pants_counter = Value('i', 0)
app = Flask(__name__)

app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload/<clothingName>', methods=['POST'])
def upload_file(clothingName):
    uploaded_file = request.files['file']

    if uploaded_file.filename != '':
        file_ext = os.path.splitext(uploaded_file.filename)[1]

        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        
        if clothingName == 'shirt':
            with shirt_counter.get_lock():
                shirt_counter.value += 1
                count = shirt_counter.value
                print('shirt', count)
        elif clothingName == 'pants':
            with pants_counter.get_lock():
                pants_counter.value += 1
                count = pants_counter.value
                print('pants', count)

        uploaded_file.save(f'images/{clothingName}{count}.png')

    return redirect('http://localhost:5173')

@app.route('/img/<filename>', methods=['GET'])
def send_image(filename):
    file_path = f'./images/{filename}.png'
    return send_file(file_path)

@app.route('/generate')
def generate_outfit():
    shirt_id = request.args.get('shirtId', 1)
    pants_id = request.args.get('pantsId', 1)
    # image_layering.run(shirt_id, pants_id)

if __name__ == '__main__':
    app.run(debug=True, port=5001)