# iMessage Flask API

Send iMessage text through Flask API.
Run this server on macOS.

## Run the Server

```bash
./main.py
```

## Test with curl

```bash
curl -X POST http://localhost:5555/send_message \
  -H "Content-Type: application/json" \
  -d '{"phone": "+12345667890", "message": "Hello from API"}'
```
