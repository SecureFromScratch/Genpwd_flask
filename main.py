from flask import Flask, request, jsonify, abort
import logging

#
# IMPORTANT: If you want to report an error use
# generate_http_exception return an http error status
# (default is status code 422 - unprocessable content)
#

app = Flask(__name__)

def generate_http_exception(error_desc: str, status_code: int = 422):
    abort(status_code, description=error_desc)

def generate_password(length: int) -> str:
	# TODO: This function currently returns a placeholder password.
	# You will need replace this logic with actual password generation logic.
	# The valid password characters are defined by VALID_LETTERS
    VALID_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*-+=_'
    
    result = 'a' * length

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
