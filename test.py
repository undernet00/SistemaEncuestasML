import requests

#BASE = "http://190.64.90.147:1000/"
BASE = "http://127.0.0.1:5000/"
#BASE = "https://modelws.azurewebsites.net:5000/"

FRASE = "Me gustaron los huevos rotos. La verdad que la atención fue muy buena. Pero el precio me pareció un poco caro. Volvería."

print ("--")
print ("Frase:" + FRASE)

response = requests.get(BASE + "modelo/" + FRASE)

#print (BASE + "modelo/" + FRASE)

print("Respuesta:" + str(response.text))


print ("--")