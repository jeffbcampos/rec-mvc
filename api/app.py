from flask import Flask
from flask_migrate import Migrate
from api.routes.bluePrints import blue_prints
from api.control.MainController import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object('config')
migrate = Migrate(app, db)
db.init_app(app)
CORS(app)
jwt = JWTManager(app)
mail = Mail(app)
for bp in blue_prints:
    app.register_blueprint(bp)

@app.route('/')
def main():
    return "A API não explodiu"


if __name__ == '__main__':
    app.run(debug=True)
