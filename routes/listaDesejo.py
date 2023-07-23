from flask import Blueprint
from control.ListaController import consultarListaDesejo, inserirListaDesejo, removerListaDesejo


listaDesejo_routes = Blueprint('listaDesejo_routes', __name__)


listaDesejo_routes.route('/listaDesejo', methods=['GET'])(consultarListaDesejo)
listaDesejo_routes.route('/inserirListaDesejo', methods=['POST'])(inserirListaDesejo)
listaDesejo_routes.route('/removerListaDesejo', methods=['POST'])(removerListaDesejo)