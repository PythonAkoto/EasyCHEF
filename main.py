import os
import typing
from flask import Flask

from homepage import home

app: Flask = Flask(__name__)

app.register_blueprint(home)

if __name__ == "__main__":
    app.run(debug=True)
