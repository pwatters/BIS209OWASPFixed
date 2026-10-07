from pathlib import Path
from flask import Flask, abort, request

app = Flask(__name__)
BASE = (Path(__file__).parent / "demo_files").resolve()
BASE.mkdir(exist_ok=True)
(BASE / "report.txt").write_text("Public report\n", encoding="utf-8")
(Path(__file__).parent / "secret.txt").write_text("INTERNAL: payroll-password-reset-notes\n", encoding="utf-8")


@app.route("/download")
def download():
    filename = request.args.get("file", "report.txt")
    path = (BASE / filename).resolve()
    if path.parent != BASE:
        abort(403)
    return f"<pre>{path.read_text(encoding='utf-8')}</pre>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)
