# python-app

A simple Python web application with a sample API built using Flask.

## Features

- Simple RESTful API endpoints
- JSON responses
- Easy to extend and customize

## API Endpoints

- `GET /` - Welcome endpoint
- `GET /api/hello` - Sample Hello World endpoint

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ajasingh2022/python-app.git
cd python-app
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python app.py
```

The app will start on `http://localhost:5000`

## Testing the API

You can test the API using curl or any HTTP client:

```bash
# Test the home endpoint
curl http://localhost:5000/

# Test the hello endpoint
curl http://localhost:5000/api/hello
```

Expected response from `/api/hello`:
```json
{
  "message": "Hello, World!",
  "status": "success"
}
```