from flask import Blueprint
from control.MailController import enviarEmail, confirmarEmail, recuperarSenha, checkToken, alterarSenha

mail_routes = Blueprint('mail_routes', __name__)

mail_routes.route('/enviarEmail', methods=['GET'])(enviarEmail)
mail_routes.route('/confirmarEmail/<token>', methods=['GET'])(confirmarEmail)
mail_routes.route('/recuperarSenha', methods=['POST'])(recuperarSenha)
mail_routes.route('/check-token/<token>', methods=['GET'])(checkToken)
mail_routes.route('/novaSenha/<token>', methods=['POST'])(alterarSenha)
