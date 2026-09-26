from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)


MONGO_URI = os.environ.get('MONGO_URI')

cliente = MongoClient(MONGO_URI)
base_datos = cliente['mascotas_db']
coleccion_consejos = base_datos['consejos']


@app.route('/')
def inicio():
    return jsonify({'mensaje': 'Microservicio de consejos para mascotas perdidas funcionando'})


@app.route('/consejos')
def obtener_consejos():
    """Consulta todos los consejos guardados en MongoDB Atlas y los devuelve en JSON."""
    consejos = list(coleccion_consejos.find({}, {'_id': 0}))
    return jsonify(consejos)


if __name__ == '__main__':
    puerto = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=puerto)
