from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    # Indented this line
    return "Welcome to my Flask API!"

@app.route('/student')
def get_student():
    # Indented this block
    return jsonify({
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    })

# Added this to allow the app to run
if __name__ == '__main__':
    app.run(debug=True)
