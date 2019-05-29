import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from speecher import Speecher
from pixabay_image_provider import PixabayImageProvider
from config import load_configuration

app = Flask(__name__)
CORS(app)

CONFIG_PATH = os.getenv("SPEECHER_CONFIG", "dev.json")
speecher_config = load_configuration(CONFIG_PATH)
provider = PixabayImageProvider(speecher_config)
speecher = Speecher(provider)

@app.route("/", methods=['GET'])
def search():
    q = request.args.get('q', None)
    if (q is not None):
        url = speecher.get_illustration_url(q)
        return jsonify(url=url)
    else:
        abort(400)
