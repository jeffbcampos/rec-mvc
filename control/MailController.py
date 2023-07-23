from flask import redirect, request, jsonify
from control.MainController import db, verificaSenha
from datetime import timedelta
from models.Verificacao import Verificacao
from models.User import Usuarios
from bcrypt import hashpw, gensalt, checkpw
from flask_jwt_extended import create_access_token, decode_token

apiUrl = 'https://api-mvc-test.vercel.app'
recUrl = 'https://rec-eight.vercel.app'

def enviarEmail():
    from api.app import mail
    from flask_mail import Message
    
    try:
        email = request.args.get('email')
        senha = request.args.get('senha')
        nome = request.args.get('nome')
        tokenEmail = create_access_token(identity=email, expires_delta=timedelta(minutes=30))
        novo_user = Verificacao(nome=nome, email=email, senha=senha, token=tokenEmail)        
        db.session.add(novo_user)
        db.session.commit()
        print(novo_user.email)        
        msg = Message('Confirmação de email', sender='project-rec@outlook.com', recipients=[f'{email}'])
        url = f'{apiUrl}/confirmarEmail/{tokenEmail}'
        msg.html = f'''        
            <p>Confirme seu cadastro através do link abaixo:</p>
            <a href="{url}">
                {url}
            </a>'''
        mail.send(msg)
        print('teste')
        return jsonify({'status': 'success', 'msg': 'Email enviado com sucesso'})
    except Exception as e:
        print(e)
        return redirect(f'{recUrl}/error404')
        
def confirmarEmail(token):
    try:
        response = db.session.query(Verificacao).filter_by(token=token, is_valid=False).all()[0]
        if response:
            db.session.query(Verificacao).filter_by(token=token).update({Verificacao.is_valid: True})
            db.session.commit()
            new_user = Usuarios(nome=response.nome, email=response.email, senha=response.senha)
            db.session.add(new_user)
            db.session.commit()
            return redirect(f'{recUrl}/finalizado?q={token}')
        else:
            return redirect(f'{recUrl}/finalizado')
    except Exception as e:
        print(e)
        return redirect(f'{recUrl}/error404')
        
        
def recuperarSenha():
    from api.app import mail
    from flask_mail import Message
    
    try:
        email= request.json['email']
        result = db.session.query(Usuarios).filter_by(email=email).first()
        if result:
            tokenEmail = create_access_token(identity=email, expires_delta=timedelta(minutes=30))
            msg = Message('Alteração de Senha', sender='project-rec@outlook.com', recipients=[f'{email}'])
            url = f'{apiUrl}/check-token/{tokenEmail}'
            msg.html = '''        
            <p>Altere sua senha através do link abaixo:</p>
            <a href="{url}">
                {url}
            </a>'''
            mail.send(msg)
            return jsonify({'status': 'success', 'msg': 'Email enviado com sucesso'})
        else:
            return jsonify({'status': 'fail', 'msg': 'Email não encontrado'})
    except Exception as e:
        return redirect(f'{recUrl}/error404')
        
        
def checkToken(token):
    try:
        decoded_token = decode_token(token)
        if decoded_token['type'] == 'access':
            return redirect(f'{apiUrl}/novaSenha?q={token}')
        else:
            return jsonify({'status': 'fail', 'msg': 'Token inválido'})
    except Exception as e:
        return redirect(f'{recUrl}/error404')
        
        
def alterarSenha(token):
    try:
        tokenConfirm = decode_token(token)
        email = tokenConfirm['sub']
        senha = request.json['senha']
        if verificaSenha(senha):
            senha = senha.encode('utf-8')
            salt = gensalt()
            senha = hashpw(senha, salt).decode('utf-8')
            db.session.query(Usuarios).filter_by(email=email).update({Usuarios.senha: senha})
            return jsonify({'status': 'success', 'msg': 'Senha alterada com sucesso'})
        else:
            return jsonify({'status': 'senhaFraca'})
    except Exception as e:
        return redirect(f'{recUrl}/error404')
            
            
        