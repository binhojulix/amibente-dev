from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    a = 10 + 10
    b = 30 + 30
    c = 30 + 30
    return "Flask inside Docker 2!!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True,host='0.0.0.0',port=port)