from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # declaring that this is the homepage
def home():
    return render_template("angela.htm")

if __name__ == "__main__":
    app.run(debug=True)