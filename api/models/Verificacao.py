from api.control.MainController import db

class Verificacao(db.Model):
    __tablename__ = 'verificacao'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    email = db.Column(db.String(255))
    senha = db.Column(db.String(255))
    is_valid = db.Column(db.Boolean, default=False)
    token = db.Column(db.String(255))
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'is_valid': self.is_valid,
            'token': self.token
        }
    
    