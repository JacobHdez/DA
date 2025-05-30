from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hola, Mundo!!!'
    
    from api.historical import historical_bp
    app.register_blueprint(historical_bp)

    return app
