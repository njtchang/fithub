from flask import Flask, abort, render_template, request, redirect, url_for, send_file
import os
from multiprocessing import Value
from image_layering import create_file


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
                count = shirt_counter.value
                shirt_counter.value += 1
                print('shirt', count)
        elif clothingName == 'pants':
            with pants_counter.get_lock():
                count = pants_counter.value
                pants_counter.value += 1
                print('pants', count)

        uploaded_file.save(f'images/{clothingName}{count}.png')

    return redirect('http://localhost:5173')

@app.route('/generate', methods=['POST'])
def generate_outfit():
    shirt_id = request.args.get('shirtId', 0)
    pants_id = request.args.get('pantsId', 0)
    create_file(shirt_id, pants_id)
    return send_file(f'./images/combo_outfit.png')

if __name__ == '__main__':
    app.run(debug=True, port=5001)