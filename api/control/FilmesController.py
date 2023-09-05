from flask import redirect, url_for, request, jsonify
from models.Filmes import Filmes
from control.MainController import db
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, decode_token

recUrl = 'https://rec-eight.vercel.app'

@jwt_required()
def consultarFilmes():
    try:
        if request.method == 'GET':
            id = get_jwt_identity()
            response = Filmes.query.filter_by(id_usuario=id).all()
            return jsonify([e.serialize for e in response])
        elif request.method == 'POST':
            titulo = request.json['titulo']
            id_usuario = get_jwt_identity()
            response = Filmes.query.filter_by(titulo=titulo,id_usuario=id_usuario).first()
            if response:
                return jsonify({'msg': 'success'})
            else:
                return jsonify({'msg': 'fail'})
    except Exception as e:
        print(e)
        return redirect(f'{recUrl}/error404')
        
        
@jwt_required()
def inserirFilme():
    try:
        titulo = request.json['titulo']
        imagem = request.json['imagem']
        nota = request.json['nota']
        tipo = request.json['tipo']
        id_api = request.json['id_api']
        id_usuario = get_jwt_identity()
        result = db.session.query(Filmes).filter_by(titulo=titulo,id_usuario=id_usuario).first()
        if result:
            return jsonify({'msg': 'fail'})
        else:
            db.session.add(Filmes(titulo=titulo, imagem=imagem, nota=nota, tipo=tipo, id_api=id_api, id_usuario=id_usuario))
            db.session.commit()
            return jsonify({'msg': 'success'})
    except Exception as e:
        return redirect(f'{recUrl}/error404')
        
        
@jwt_required()
def removerFilme():
    try:
        titulo = request.json['titulo']
        id_usuario = get_jwt_identity()
        result = db.session.query(Filmes).filter_by(titulo=titulo,id_usuario=id_usuario).first()
        if result:
            db.session.delete(result)
            db.session.commit()
            return jsonify({'msg': 'success'})
        else:
            return jsonify({'msg': 'fail'})
    except Exception as e:
        return redirect(f'{recUrl}/error404')
        
