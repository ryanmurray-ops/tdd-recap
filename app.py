from flask import Flask

app = Flask(__name__)

@app.route("/")
def list_duties():
    return ['duty1', 'duty2', 'duty3', 'duty4', 'duty5', 'duty6', 'duty7', 'duty8', 'duty9', 'duty10', 'duty11', 'duty12', 'duty13']