
from flask import Flask, render_template, request

from db import add_duty, get_all_duties, get_error_message

app = Flask(__name__)

@app.route("/")
def list_duties():
    duties = get_all_duties()
    error = get_error_message()
    return render_template("index.html", duties=duties, error=error)

@app.route("/add-duty", methods=["POST"])
def add_duty_route():
    new_duty = {
        "identifier": request.form["identifier"],
        "description": request.form["description"]

    }
    
    add_duty(new_duty)
    error = get_error_message()

    duties = get_all_duties()

    return render_template("index.html", duties=duties, error=error)

if __name__ == "__main__":
    app.run(debug=True)