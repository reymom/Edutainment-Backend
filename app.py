import re
from flask import Flask, jsonify, request
from flask_cors import CORS
from api.story_generator import generate_story_text
from api.question_generator import generate_questionnaire_object
from api.image_generator import generate_image
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)
CORS(app, resources={r"/generate_story": {"origins": "http://localhost:3000"},
                     r"/generate_questionnaire": {"origins": "http://localhost:3000"}})


@app.route('/generate_story', methods=['POST'])
def generate_story():
    images = request.json.get('images')
    prompt = request.json.get('prompt')
    width = request.json.get('width')
    height = request.json.get('height')
    img_type = request.json.get('format')

    story_text_response = generate_story_text(
        prompt, images[0], width, height, img_type)
    return jsonify(story_text_response.__dict__)


@app.route('/generate_questionnaire', methods=['POST'])
def generate_questionnaire():
    story_text = request.json.get('story_text')
    questionnaire_response = generate_questionnaire_object(story_text)
    return jsonify(questionnaire_response.__dict__)


@app.route('/generate_image', methods=['POST'])
def generate_image_route():
    story_text = request.json.get('story_text')
    image_response = generate_image(story_text)
    return jsonify(image_response.__dict__)


if __name__ == '__main__':
    app.run(debug=True)
