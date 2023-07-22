from flask import Blueprint
from api.control.FilmesController import consultarFilmes, inserirFilme

filmes_routes = Blueprint('filmes_routes', __name__)

filmes_routes.route('/filmes', methods=['GET', 'POST'])(consultarFilmes)
filmes_routes.route('/inserirFilme', methods=['POST'])(inserirFilme)
