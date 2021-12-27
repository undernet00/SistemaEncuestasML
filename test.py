import requests

BASE = "http://127.0.0.1:5000/"

FRASE = "La comida estaba muy rica. Especialmente el pollo. No así la milanesa. Creo que vamos a volver. Gracias por la buena atención.}"
#FRASE = "frase"

response = requests.get(BASE + "modelo/" + FRASE)

print (BASE + "modelo/" + FRASE)

print(response.json())
