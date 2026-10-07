import hashlib
import json
import os
import secrets
import subprocess

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")


def hash_password(password):
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)
    return salt.hex() + ":" + digest.hex()


def ping(host):
    subprocess.run(["ping", "-c", "1", host], check=False)


def load_data(data):
    return json.loads(data)


if __name__ == "__main__":
    print("Run: bandit 03_bandit_fixed.py")
