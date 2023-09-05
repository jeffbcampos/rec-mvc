from flask import request, jsonify,redirect
from control.MainController import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.ListaDesejo import ListaDesejo

recUrl = 'https://rec-eight.vercel.app'

@jwt_required()
def consultarListaDesejo():
    try:
        id = get_jwt_identity()
        response = db.session.query(ListaDesejo).filter_by(id_usuario=id).all()
        return jsonify([e.serialize for e in response])
    except Exception as e:
        return redirect(f'{recUrl}/error404')
        
        
@jwt_required()
def inserirListaDesejo():
    try:
        id = get_jwt_identity()
        titulo = request.json['titulo']
        imagem = request.json['imagem']
        nota = request.json['nota']
        tipo = request.json['tipo']
        id_api = request.json['id_api']
        lista = ListaDesejo(titulo=titulo, imagem=imagem, nota=nota, tipo=tipo, id_api=id_api, id_usuario=id)
        db.session.add(lista)
        db.session.commit()
        return jsonify({'status': 'success'})
    except Exception as e:
        return redirect(f'{recUrl}/error404')
        
        
@jwt_required()
def removerListaDesejo():
    try:
        titulo = request.json['titulo']
        id_usuario = get_jwt_identity()
        db.session.query(ListaDesejo).filter_by(titulo=titulo, id_usuario=id_usuario).delete()
        return jsonify({'status': 'success'})
    except Exception as e:
        return redirect(f'{recUrl}/error404')


