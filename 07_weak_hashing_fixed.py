import hashlib
import secrets

password = input("Password: ")
salt = secrets.token_bytes(16)
digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)
print("Salt:", salt.hex())
print("PBKDF2:", digest.hex())
print("Run it again with the same password: a new salt gives a different stored value.")
