# Flask Key Generator Microservice

## Overview
This is a Flask-based REST API microservice for generating random encryption keys for the **Caesar Cipher** and **Vigenère Cipher** algorithms. It is designed to be lightweight, easy to use, and compatible with other microservices in the project.

---

## Features
1. **Caesar Cipher Key Generation:**
   - Generates a random integer key between 1 and 25.

2. **Vigenère Cipher Key Generation:**
   - Generates a random string key of customizable length (default: 5).

3. **Error Handling:**
   - Provides meaningful error messages with appropriate HTTP status codes for invalid inputs.

---

## API Endpoints
### 1. Generate Caesar Cipher Key
- **Endpoint:** `/generate-key/caesar`
- **Method:** `GET`
- **Description:** Generates a random integer key for the Caesar Cipher.
- **Example Request:**
    ```bash
    curl http://127.0.0.1:5000/generate-key/caesar
    ```
- **Example Response:**
    ```json
    {
      "key": 14
    }
    ```

---

### 2. Generate Vigenère Cipher Key
- **Endpoint:** `/generate-key/vigenere`
- **Method:** `GET`
- **Query Parameter:**
    - `length` (optional): Specifies the length of the key. Default is 5. Minimum is 2.
- **Example Request:**
    ```bash
    curl "http://127.0.0.1:5000/generate-key/vigenere?length=7"
    ```
- **Example Response:**
    ```json
    {
      "key": "GHIJKLM"
    }
    ```

---

## Running the Microservice Locally
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/celeresx/flask-key-generator.git
   cd flask-key-generator
