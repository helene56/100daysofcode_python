from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/") # declaring that this is the homepage
def hello_world():
    return "<p>Hello, World!</p>"

# enables you to run the file from the IDE
# checks that the script is running from current file, it is the top level
if __name__ == "__main__":
    app.run()