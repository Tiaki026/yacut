from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import os
from yacut.yacut import app


SWAGGER_URL = '/api/docs'
API_URL = '/openapi.yml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Дополнительные конфигурации
        'app_name': "Test application"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/openapi.yml')
def send_openapi():
    return send_from_directory(os.getcwd(), 'openapi.yml')


@app.route('/')
def index():
    return "API Documentation available at /api/docs"


if __name__ == '__main__':
    app.run(debug=True)
