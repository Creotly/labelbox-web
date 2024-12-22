from flask import Flask
from flask_cors import CORS
from routes.annotation import annotation

app = Flask(__name__)
CORS(app)

app.register_blueprint(annotation)

if __name__ == "__main__":
    app.run(debug=True)
