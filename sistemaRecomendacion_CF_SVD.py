import csv
import math
import pprint
import operator
from time import sleep
import sys

# Función para cargar datos de los CSV

def cargarBD():
	tags = []
	with open('./rs-cour-dataset/movie-tags.csv','r',encoding="utf8") as f:
		entradas = csv.reader(f,delimiter=',',quoting=csv.QUOTE_ALL)
		for reg in entradas:
			tags.append(reg)

	titles = {}
	with open('./rs-cour-dataset/movie-titles.csv','r',encoding="utf8") as f:
		entradas = csv.reader(f,delimiter=',',quoting=csv.QUOTE_ALL)
		for reg in entradas:
			titles[reg[0]] = reg[1]

	ratings = {}
	with open('./rs-cour-dataset/ratings.csv','r',encoding="utf8") as f:
		entradas = csv.reader(f,delimiter=',',quoting=csv.QUOTE_ALL)
		for reg in entradas:
			if reg[1] not in ratings:
				ratings[reg[1]] = {}
			ratings[reg[1]][reg[0]] = float(reg[2])

	# Añadir la valoración media a cada producto
	for key in ratings:
		suma = 0.0
		for rate in ratings[key].values():
			suma += rate
		
		ratings[key]['MEDIA_RATING'] = suma/len(ratings[key])

	users = {}
	with open('./rs-cour-dataset/users.csv','r',encoding="utf8") as f:
		entradas = csv.reader(f,delimiter=',',quoting=csv.QUOTE_ALL)
		for reg in entradas:
			users[reg[0]] = reg[1]

	return tags,titles,ratings,users

######################################################################
#### IMPLEMENTACIÓN DEL SISTEMA DE RECOMENDACIÓN CF BASADO EN SVD ####
######################################################################

'''

    QUÉ SABEMOS

    1.- Matriz dispersa con:
        a) Columnas -> Usuarios
        b) Películas -> Laterales
        c) Celda -> Ranking en [1, 5]

'''


def mostrarResultados(idUser,recomendaciones,dicTitulos):
	print("Top 10 recommendations for user "+idUser+":")
	cont=1
	for reco in recomendaciones:
		print(reco[0] + ', ' + dicTitulos[reco[0]] + ", " + str(reco[1]))
		cont+=1

if __name__ == "__main__":

	tags, titles, ratings_per_product, users = cargarBD()
	
	# correlationItemItem = modelItemItem(ratings_per_product,titles)

	while(True):
		idUser = input("Introduce el id del usuario activo para el que quiera obtener una recomendación:")
		
		# mostrarResultados(idUser,PredictionFunction(idUser, ratings_per_product,correlationItemItem)[:10],titles)