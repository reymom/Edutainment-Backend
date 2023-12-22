import requests
import base64
from PIL import Image


def generate_story():
    img_path = '/home/reymon/Descargas/Raman_the_horse_trainer.jpg'
    img = Image.open(img_path)
    img_bytes = img.tobytes()
    width, height = img.size
    # Encode the bytes in base64
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')

    api_url = 'http://localhost:5000/generate_story'

    # Payload with the base64 encoded image
    payload = {
        "prompt": "Write an accurate introduction of a story for small kids given the image with the following theme: adventure. Write a maximum of 125 words.",
        "images": [img_base64],
        "width": width,
        "height": height,
        "format": "JPEG"
    }
    return requests.post(api_url, json=payload)


def generate_questionnaire(story_text):
    api_url = 'http://localhost:5000/generate_questionnaire'

    payload = {
        "story_text": story_text
    }
    return requests.post(api_url, json=payload)


response = generate_story()
print(response.json())
response = generate_questionnaire(response.json().get('story_text', ''))
print(response.json())
