from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route("/") # declaring that this is the homepage
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>\
        <p>this is a paragraph</p>\
        <iframe src="https://giphy.com/embed/K1tgb1IUeBOgw" width="480" height="278" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'




@app.route("/bye") # when accesing url/bye the page will display "Bye"
def say_bye():
    return "Bye"

# when using <> it will use it as a variable, so whatever gets input will now display in name in the function
# using type:variable makes it possible to use that path as a specific variable
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"hello there {name}, you are {number}"

# enables you to run the file from the IDE
# checks that the script is running from current file, it is the top level
# use debug to avoid having to shut and reopen server when making changes
if __name__ == "__main__":
    app.run(debug=True)