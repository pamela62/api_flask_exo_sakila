# Le model sert à communiquer avec notre base de données Salika
#import des librairies
from flask import request, jsonify, abort
from flask_mysqldb import MySQL
#import du controller
from app.controllers.filmController import filmController
filmController = filmController()

class Film:

    #Définissions des variables de classe
    def __init__(self,film_id = None, title=None, description=None, release_year=None, language_id=None, original_language_id=None, rental_duration=None, rental_rate=None, length=None,replacement_cost=None,rating=None, special_features=None,last_update=None):
        self.film_id = film_id,
        self.title = title,
        self.description = description,
        self.release_year = release_year,
        self.language_id = language_id,
        self.original_language_id = original_language_id,
        self.rental_duration = rental_duration,
        self.rental_rate = rental_rate,
        self.length = length,
        self.replacement_cost = replacement_cost,
        self.rating = rating,
        self.special_features = special_features,
        self.last_update = last_update

    #Méthode pour récupérer tous les films
    def get_all_film(self):
        try :
            cur=MySQL.connection.cursor()
            cur.execute("SELECT * FROM sakila.film")
            reponse = cur.fetchall()
            cur.close()
            return reponse
        except Exception as e:
            return e

    #Methode pour récupérer un film à partir de son id
    def get_article_by_id(self, film_id):
        try :
            cur=MySQL.connection.cursor()
            cur.execute("SELECT * FROM sakila.film WHERE film_id=%s",(str(film_id),))
            reponse = cur.fetchone()
            cur.close()
            return reponse
        except:
            return False