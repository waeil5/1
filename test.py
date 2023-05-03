from flask import Flask, render_template
app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("about.html", title="About US", test= "This is my About US page")

@app.route("/home")
def homepage():
    return render_template("home.html", title= "Home Page", custom="home it")

@app.route("/add")
def add():
    return render_template("add.html", title= "Add Skill", custom="add it")

if __name__=="__main__":
    app.run(debug=True, port=3000)
