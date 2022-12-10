# importing flask
from flask import Flask
from flask_migrate import Migrate

# defining function for app factory
def create_app():
    app = Flask(__name__)

    # database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hello123@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # index route
    @app.route('/')
    def hello():
        return 'Hello, PetFax!'
    
    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)
    
    return app