from flask import Flask

app = Flask(__name__)

app.secret_key = b'\xd4\x84\xb8\x1dU\xbc]p\xf6\xe2r\xf2q\x95L\x01'

from src.demo import routes
