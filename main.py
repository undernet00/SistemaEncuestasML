from flask import Flask
from flask_restful import Api, Resource
import spacy
import json


app = Flask(__name__)
api = Api(app)


class Modelo(Resource):
    def get(self, frase):

        model_path = 'model-best'
        model = spacy.load(model_path)
        labels = []
        doc = model(frase).doc

        for ent in doc.ents:
            #print(ent)
            #print(ent.label_)
            labels.append(ent.label_)
            
        return {"labels": (json.dumps(labels))}


api.add_resource(Modelo, "/modelo/<string:frase>/")
if __name__ == "__main__":
    app.run(debug=True)
