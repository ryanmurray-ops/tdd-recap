from flask import Flask

app = Flask(__name__)

@app.route("/")
def list_duties():
    return ['duty1', 'duty2']