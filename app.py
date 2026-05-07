from flask import Flask, render_template, request

from db import get_all_duties

app = Flask(__name__)

@app.route("/")
def list_duties():
    database_duties = get_all_duties()
    return render_template("index.html", duties= database_duties)

@app.route("/add-duty", methods=["POST"])
def add_duty():
    new_duty = {
        "identifier": request.form["identifier"],
        "description": request.form["description"]

    }
    
    return new_duty

if __name__ == "__main__":
    app.run(debug=True)