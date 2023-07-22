from flask import Blueprint
from api.control.SeriesController import consultarSeries, inserirSerie, removerSerie

series_routes = Blueprint('series_routes', __name__)

series_routes.route('/series', methods=['GET', 'POST'])(consultarSeries)
series_routes.route('/inserirSerie', methods=['POST'])(inserirSerie)
series_routes.route('/removerSerie', methods=['POST'])(removerSerie)
