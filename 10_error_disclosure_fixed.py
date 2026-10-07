import logging
import sqlite3
from flask import Flask

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.route("/account")
def account():
    try:
        conn = sqlite3.connect("missing_database.db")
        conn.execute("SELECT secret_column FROM missing_table").fetchone()
        return "OK"
    except Exception:
        app.logger.exception("Account lookup failed")
        return "Something went wrong. Please try again later.", 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5005, debug=False)
