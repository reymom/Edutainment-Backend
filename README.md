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

## Testing

```bash
python test_requests.py
```
