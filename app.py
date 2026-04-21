from flask import Flask

app = Flask(__name__)

@app.route("/")
def list_duties():
    return [
                    {"Duty Number": 1, "Description": "Duty 1 description"},
                    {"Duty Number": 2, "Description": "Duty 2 description"},
                    {"Duty Number": 3, "Description": "Duty 3 description"},
                    {"Duty Number": 4, "Description": "Duty 4 description"},
                    {"Duty Number": 5, "Description": "Duty 5 description"},
                    {"Duty Number": 6, "Description": "Duty 6 description"},
                    {"Duty Number": 7, "Description": "Duty 7 description"},
                    {"Duty Number": 8, "Description": "Duty 8 description"},
                    {"Duty Number": 9, "Description": "Duty 9 description"},
                    {"Duty Number": 10, "Description": "Duty 10 description"},
                    {"Duty Number": 11, "Description": "Duty 11 description"},
                    {"Duty Number": 12, "Description": "Duty 12 description"},
                    {"Duty Number": 13, "Description": "Duty 13 description"} 
                ]