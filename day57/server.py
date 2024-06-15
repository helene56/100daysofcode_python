from flask import Flask, render_template
import random
from datetime import datetime
import requests


agify_url = "https://api.agify.io?name="
genderize_url = "https://api.genderize.io?name="


app = Flask(__name__)

current_datetime = datetime.now()

@app.route("/") # declaring that this is the homepage
def home():
    return render_template("index copy.html")

@app.route("/guess/<name>") # declaring that this is the homepage
def guess(name):
    response = requests.get(agify_url + name)
    data = response.json()
    AGE = data["age"]
    response = requests.get(genderize_url + name)
    data_2 = response.json()
    GENDER = data_2["gender"]
    
    return render_template("index.html", name=name, age=AGE, gender=GENDER)

if __name__ == "__main__":
    app.run(debug=True)