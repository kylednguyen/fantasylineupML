from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Fantasy Football Predictor API"

if __name__ == "__main__":
    app.run(debug=True)
