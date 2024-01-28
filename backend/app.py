from flask import Flask, abort, render_template, request, redirect, url_for, send_file, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json
import os
from multiprocessing import Value
from image_layering import create_file
from PIL import Image


counter = Value('i', 0)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clothes.db'
db = SQLAlchemy(app)
app.app_context().push()
CORS(app)

class Clothing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clothingType = db.Column(db.String(5), nullable=False)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Clothing {self.id}>'
    
class ClothingObj:
    def __init__(self, id, clothingType, name):
        self.id = id
        self.clothingType = clothingType
        self.name = name
        print(json.dumps(self.to_dict()))

    def to_dict(self):
        return {'id': self.id, 'clothingType': self.clothingType, 'name': self.name}

app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jpeg']

@app.route('/upload/<clothingType>/<clothingName>', methods=['POST'])
def upload_file(clothingType, clothingName):
    uploaded_file = request.files['file']

    print(clothingName)

    if uploaded_file.filename != '':
        file_ext = os.path.splitext(uploaded_file.filename)[1]

        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        
        with counter.get_lock():
            initial_count = counter.value
        if initial_count <= 20:
            with counter.get_lock():
                counter.value += 1
            new_clothing = Clothing(clothingType=clothingType, name=clothingName)
            
            try:
                db.session.add(new_clothing)
                db.session.commit()
            except:
                return 'There was an issue adding clothing to db'

            print('uploaded!')
            save_path = f'images/{clothingType}{new_clothing.id}.{file_ext}'
            uploaded_file.save(save_path)
            if file_ext == '.jpg':
                img = Image.open(save_path)
                img.save(f'images/{clothingType}{new_clothing.id}.png')
                os.remove(save_path)

    return redirect('http://localhost:5173')

@app.route('/generate/<shirtId>/<pantsId>', methods=['POST'])
def generate_outfit(shirtId, pantsId):
    create_file(shirtId, pantsId)
    return send_file(f'./images/combo_outfit.png')

@app.route('/getShirts', methods=['GET'])
def get_shirts():
    shirts = Clothing.query.filter(Clothing.clothingType == 'shirt').all()
    print(shirts)
    return [ClothingObj(shirt.id, shirt.clothingType, shirt.name).to_dict() for shirt in shirts]

@app.route('/getPants', methods=['GET'])
def get_pants():
    pants = Clothing.query.filter(Clothing.clothingType == 'pants').all()
    return [ClothingObj(pant.id, pant.clothingType, pant.name).to_dict() for pant in pants]

@app.route('/deleteClothing/<clothingId>', methods=['DELETE'])
def deleteClothing(clothingId):
    clothing_to_delete = Clothing.query.get_or_404(clothingId)

    try:
        db.session.delete(clothing_to_delete)
        db.session.commit()
        return redirect('http://localhost:5173')
    except:
        return 'There was a problem deleting the clothing'


if __name__ == '__main__':
    app.run(debug=True, port=5001)


# TODO: jpg to png converter
# TODO: delete button
# TODO: deploy