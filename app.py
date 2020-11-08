from flask import Flask, request
from suggester import process_input_text


app = Flask(__name__)


@app.route("/analyze-sentence", methods=["POST"])
def analyze_sentence():
    input_data = request.get_json()
    text = input_data['text']
    min_prob = input_data['min_prob']
    return process_input_text(text, min_prob).to_json()


app.run()
