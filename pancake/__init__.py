from typing import Any, Dict

from flask import Flask, render_template


def index_page():
    return render_template('index.html')


def create_app(config: Dict[str, Any] = None):
    app = Flask(__name__)
    if config:
        app.config.from_mapping(config)
    app.add_url_rule('/', 'index', index_page)
    return app
