from abc import ABC, abstractmethod

from flask import Flask, request, jsonify, abort
import secrets as random  # Cryptographically secure random
import logging

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 50

class BoundedInt(ABC, int):
    @property
    @abstractmethod
    def MIN_BOUND(self) -> int:
        pass

    @property
    @abstractmethod
    def MAX_BOUND(self) -> int:
        pass

    def __init__(self, value):
        try:
                value = int(value)
        except:
            raise ValueError(f'Value must be convertible to integer')
        if not (self.MIN_BOUND <= value < self.MAX_BOUND):
            raise ValueError(f"Value must be between {self.MIN_BOUND} and {self.MAX_BOUND}")
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

app = Flask(__name__)

def generate_http_exception(error_desc: str, status_code: int = 422):
    abort(status_code, description=error_desc)

def generate_password(length: int) -> str:
    VALID_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*-+=_'
    
    result = ''.join(
        random.choice(VALID_LETTERS) for _ in range(length)
    )

    return result

class PasswordLength(BoundedInt):
    MIN_BOUND: int = MIN_PASSWORD_LENGTH
    MAX_BOUND: int = MAX_PASSWORD_LENGTH

@app.route("/genpwd", methods=['GET'])
def genpwd_route():
    length = request.args.get('length', type=PasswordLength)
    if length is None:
        generate_http_exception("A valid length parameter is required")

    password = generate_password(length)
    return jsonify(password=password)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
