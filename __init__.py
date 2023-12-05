import os
from flask import Flask

#OJO en caso de error modificar linea 9 variable de entorno
def create_app():
	app = Flask(__name__)

	app.config.from_mapping(
		SENDGRID_KEY = os.environ.get('SENDGRID_KEY'),
	)

	from . import portfolio

	app.register_blueprint(portfolio.bp)

	return app