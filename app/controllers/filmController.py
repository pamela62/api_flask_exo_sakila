# le controller sert à piloter le tout.
from flask import abort, request, url_for
from app.services.filmService import filmService

class FilmControllers:
#Creation d'une class qui fait appel au service FilmServices
    def __init__(self):
        self.filmServices = filmService()

    # Création d'une méthode qui récupère tous les films
    def get_films(self):
        return self.filmServices.get_all()

    #Méthode qui permet de récupérer un film par son id
    def get_film_by_id(self, film_id):    
        film = self.filmServices.get_film_by_id(film_id)
        if film is False:
            abort(404)
        return film