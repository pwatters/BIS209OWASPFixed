from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return render_template_string("<h1>Hello {{ name }}</h1>", name=name)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
