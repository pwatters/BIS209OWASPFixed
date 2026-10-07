from pathlib import Path
from uuid import uuid4
from flask import Flask, abort, request, send_from_directory

app = Flask(__name__)
UPLOADS = Path(__file__).parent / "safe_uploads"
UPLOADS.mkdir(exist_ok=True)
ALLOWED = {".txt", ".png", ".jpg", ".jpeg"}

FORM = '''
<h2>Upload a file</h2>
<form method="post" enctype="multipart/form-data">
  <input type="file" name="file">
  <button>Upload</button>
</form>
'''


@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        f = request.files["file"]
        ext = Path(f.filename).suffix.lower()
        if ext not in ALLOWED:
            abort(400, "File type not allowed")
        safe_name = uuid4().hex + ext
        f.save(UPLOADS / safe_name)
        return f'Uploaded safely as <a href="/uploads/{safe_name}">{safe_name}</a>'
    return FORM


@app.route("/uploads/<path:name>")
def uploaded(name):
    return send_from_directory(UPLOADS, name, as_attachment=True)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5003, debug=False)
