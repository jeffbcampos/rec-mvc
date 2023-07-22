from flask import Blueprint
from api.control.UserController import checarUsuarios, atualizarUsuario, atualizarSenha, inserirUsuario, deletarUsuario

users_routes = Blueprint('users_routes', __name__)


users_routes.route('/usuarios', methods=['POST'])(checarUsuarios)
users_routes.route('/atualizarUsuario', methods=['POST'])(atualizarUsuario)
users_routes.route('/atualizarSenha', methods=['POST'])(atualizarSenha)
users_routes.route('/inserirUsuario', methods=['POST'])(inserirUsuario)
users_routes.route('/deletarUsuario', methods=['POST'])(deletarUsuario)
