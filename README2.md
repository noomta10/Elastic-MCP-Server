# Project Galaxy: Data Retrieval API
A high-performance Python backend for querying astronomical data.

## Installation
Use the provided `requirements.txt`:
`pip install -r requirements.txt`

## Endpoints
- `GET /api/stars`: Returns a list of known stars.
- `GET /api/planets`: Returns planet details.

## Troubleshooting
If you receive a 401 error, check your `API_KEY` in the `.env` file.