import time
from flask import Flask, request

app = Flask(__name__)
PASSWORD = "orange42"
FAILURES = {}
LIMIT = 3
WINDOW = 30


@app.route("/login", methods=["POST"])
def login():
    client = request.remote_addr or "unknown"
    now = time.time()
    recent = [t for t in FAILURES.get(client, []) if now - t < WINDOW]
    FAILURES[client] = recent

    if len(recent) >= LIMIT:
        return "TOO MANY ATTEMPTS - TRY LATER", 429

    password = request.form.get("password", "")
    if password == PASSWORD:
        FAILURES[client] = []
        return "LOGIN SUCCESSFUL", 200

    FAILURES[client].append(now)
    return "LOGIN FAILED", 401


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5004, debug=False)
