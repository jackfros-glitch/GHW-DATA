from flask import jsonify, abort
from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA256())
digest.update(b"data to hash")
print(digest.finalize())


def json_abort(status_code, data=None):
    response = jsonify(data)
    response.status_code = status_code
    abort(response)

def generate_hash(password):
    digest = hashes.Hash(hashes.SHA256())
    byte_password = password.encode()
    digest.update(byte_password)
    return digest.finalize()

def check_hash(password_hash, password_string):
    return password_hash == generate_hash(password_string)