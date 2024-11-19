from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

@app.route('/generate-key/caesar', methods=['GET'])
def generate_caesar_key():
    """
    Generate a random key for Caesar Cipher.
    The key is an integer between 1 and 25.
    """
    key = random.randint(1, 25)
    return jsonify({"key": key})

@app.route('/generate-key/vigenere', methods=['GET'])
def generate_vigenere_key():
    """
    Generate a random key for Vigenère Cipher.
    The key is a string of uppercase letters with a default length of 5.
    The length can be modified via query parameters.
    """
    length = request.args.get('length', default=5, type=int)
    if length < 2:
        return jsonify({"error": "Key length must be at least 2"}), 400
    key = ''.join(random.choice(string.ascii_uppercase) for _ in range(length))
    return jsonify({"key": key})

if __name__ == '__main__':
    app.run(debug=True)
