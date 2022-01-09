from flask import Flask
from flask_restful import Api, Resource
import spacy
import json


app = Flask(__name__)
api = Api(app)
model = spacy.load('model-best')


class Modelo(Resource):
    def get(self, frase):
        labels = []
        doc = model(frase).doc

        for ent in doc.ents:
            labels.append(ent.label_)

        print(labels)

        return labels
        

api.add_resource(Modelo, "/modelo/<string:frase>/")
if __name__ == "__main__":
    app.run(host='0.0.0.0')
