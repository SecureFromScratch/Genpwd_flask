from flask import Flask, request, jsonify, abort
import random
import logging

app = Flask(__name__)

def generate_http_exception(error_desc: str, status_code: int = 422):
    abort(status_code, description=error_desc)

def generate_password(length: int) -> str:
    VALID_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*-+=_'
    
    result = ''.join(
        random.choice(VALID_LETTERS) for _ in range(length)
    )

    return result

@app.route("/genpwd", methods=['GET'])
def genpwd_route():
    length = request.args.get('length', type=int)
    if length is None:
        generate_http_exception("Length parameter is required")

    password = generate_password(length)
    return jsonify(password=password)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
