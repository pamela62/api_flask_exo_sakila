from flask import request, url_for
from datetime import date, datetime
import enum

class filmServices:

    #fonction pour creer un film à partir d'un film de ma bdd
    def make_film(self, film_bdd):
        list_film = list(film_bdd)
        newFilm = {}
        if list_film[0] != None:
            newFilm["film_id"]=int(list_film[0])
        else:
            newFilm["film_id"] = ""

        newFilm["title"]=str(list_film[1])
        newFilm["description"]=str(list_film[2])

        if list_film[3] != None:
            newFilm["release_year"]= date.year(list_film[3])  
        else :
            newFilm["release_year"]=""

        if list_film[4] != None:
            newFilm["language_id"]=int(list_film[4])
        else :
            newFilm["language_id"]=""

        if list_film[5] != None:
            newFilm["original_language_id"]=int(list_film[5])
        else :
            newFilm["original_language_id"]=""

        if list_film[6] != None:
            newFilm["rental_duration"]=int(list_film[6])
        else:
            newFilm["rental_duration"]=""

        if list_film[7] != None:
            newFilm["rental_rate"]=float(list_film[7])
        else :
            newFilm["rental_rate"]=""

        if list_film[6] != None:
            newFilm["length"]=int(list_film[6])
        else:
            newFilm["length"]=""
        
        if list_film[7] != None:
            newFilm["replacement_cost"]=float(list_film[7])
        else :
            newFilm["replacement_cost"]=""

        newFilm["rating"]=enum(list_film[6])

        if list_film[7] != None:
            newFilm["replacement_cost"]=float(list_film[7])
        else:
            newFilm["replacement_cost"] = ""

        newFilm["special_features"]=enum(list_film[6])
        newFilm["last_update"]=date.fromtimestamp(list_film[7])

        return newFilm


    #fonction pour creer une url de facon dynamique à partir d'un film
    def make_public_film(self,film):
        publicFilm = {}
        #gerer l'id
        for argument in film:         
            publicFilm[argument]=film[argument]
        return publicFilm