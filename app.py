from flask import Flask, render_template, request

from db import add_duty, get_all_duties

app = Flask(__name__)

@app.route("/")
def list_duties():
    duties = get_all_duties()
    return render_template("index.html", duties = duties)

@app.route("/add-duty", methods=["POST"])
def add_duty_route():
    new_duty = {
        "identifier": request.form["identifier"],
        "description": request.form["description"]

    }
    
    add_duty(new_duty)

    duties = get_all_duties()

    return render_template("index.html", duties = duties)

if __name__ == "__main__":
    app.run(debug=True)