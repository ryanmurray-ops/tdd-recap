from flask import Flask, render_template

from db import get_all_duties

app = Flask(__name__)

@app.route("/")
def list_duties():
    database_duties = get_all_duties()
    return render_template("index.html", duties= database_duties)

class Duty:
    def __init__(self, identifier, description):
        self.identifier = identifier
        self.description = description

if __name__ == "__main__":
    app.run(debug=True)