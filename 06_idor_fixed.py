from flask import Flask, abort, request

app = Flask(__name__)

INVOICES = {
    1001: {"owner": "alice", "amount": 1250, "description": "Laptop"},
    1002: {"owner": "bob", "amount": 4800, "description": "Server"},
}


@app.route("/invoice/<int:invoice_id>")
def invoice(invoice_id):
    current_user = request.args.get("as", "alice")
    record = INVOICES.get(invoice_id)
    if not record:
        abort(404)
    if record["owner"] != current_user:
        abort(403)
    return f"Logged in as {current_user}<br>Invoice {invoice_id}: {record}"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=False)
