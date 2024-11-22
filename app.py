from flask import Flask
from logger import logging

app = Flask(__name__)



@app.route('/', methods = ['GET', 'POST'])
def index():
    logging.info("U have successfully done ur logging")
    return "This is my ML PROJECT"

if __name__ == "__main__":
    app.run(debug=True)