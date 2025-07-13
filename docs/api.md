# API Documentation

## POST /chat
- Description: Send a message to the LLM and get a response
- Request Body:
```json
{ "message": "Hello" }
```
- Response:
```json
{ "response": "Hi there!" }
```

## GET /health
- Description: Check if the server is running
- Response:
```json
{ "status": "ok" }
```
