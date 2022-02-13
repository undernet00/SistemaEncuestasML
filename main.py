from distutils.log import debug
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import spacy
import json


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app)
model = spacy.load('model-best')


class Modelo():
    def get(frase):
        labels = []
        doc = model(frase).doc
        
        for ent in doc.ents:
            labels.append(ent.label_)
            #print(ent)

        #print(labels)
        return labels
        
# ...
@app.route('/modelo', methods=['POST'])
def procesa_json():
    content_type = request.headers.get('Content-Type')
    #print("content_type: " + content_type)
    #print("request.charset: " + request.charset)
    
    if (content_type == 'application/json'):
        #Acción
        mensaje = request.json['mensaje']
        analisis = Modelo.get(mensaje)
        jeison = jsonify(analisis)
        return jeison
        

        return jsonify(datos)
    else:
        return 'Content-Type not supported!'

if __name__ == "__main__":
    app.run(host='0.0.0.0') 