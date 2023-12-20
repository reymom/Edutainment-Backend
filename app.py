from flask import Flask, jsonify, request
from api.gemini import generate_questionnaire, generate_story_text
from api.image_generator import generate_image
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
app = Flask(__name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


@app.route('/generate_story', methods=['POST'])
def generate_story():
    image = request.json.get('image')
    prompt = request.json.get('prompt')

    story_text_response = generate_story_text(image, prompt)
    return jsonify(story_text_response.__dict__)


@app.route('/generate_questionnaire', methods=['POST'])
def generate_questionnaire():
    story_text = request.json.get('story_text')
    questionnaire_response = generate_questionnaire(story_text)
    return jsonify(questionnaire_response.__dict__)


@app.route('/generate_image', methods=['POST'])
def generate_image_route():
    story_text = request.json.get('story_text')
    image_response = generate_image(story_text)
    return jsonify(image_response.__dict__)


if __name__ == '__main__':
    app.run(debug=True)
