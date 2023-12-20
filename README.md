# Edutainment-Backend

## Development

1. Install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

2. Run the Flask API

```bash
export FLASK_APP=app
export FLASK_ENV=development # Set to "production" for production environment
python app.py
```

(On Windows, use set instead of export.)

## Test

```bash
curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Write a short accurate story by looking at images carefully and make it a small kids story.", "images":["base64_encoded_image1", "base64_encoded_image2"]}' http://localhost:5000/generate_gemini_text
```
