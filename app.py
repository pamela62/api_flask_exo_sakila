# Importer flask
from app.controllers.filmController import FilmController
from flask import Flask, jsonify, abort, request
from flask.helpers import make_response, url_for

from app import app

#Creation de la route qui permet de récupérer la liste de films :
@app.route("/films",methods=["GET"])
def get_film():
    return jsonify(FilmController.get_films())


#Creation de la route qui permet de récupérer un film par son id
@app.route("/films/<int:film_id>",methods=["GET"])
def get_film_by_id(film_id):
    if FilmController.get_film_by_id(film_id) is False:
        abort(404)
    return jsonify(FilmController.get_film_by_id(film_id))