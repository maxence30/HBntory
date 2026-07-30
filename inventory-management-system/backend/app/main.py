from flask import Flask

from app.routes.auth_routes import auth_bp
from app.routes.user_routes import user_bp
from app.routes.stock_routes import stock_bp


def create_app():

    app = Flask(__name__)

    app.secret_key = "dev_secret_key"

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(stock_bp)

    return app


if __name__ == "__main__":

    app = create_app()

    app.run(debug=True)