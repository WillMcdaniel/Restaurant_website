from flask import Flask, render_template
app = Flask(__name__)

#this is the main route

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index.html')
def homepage():
    return render_template("index.html")


@app.route('/threecolumn.html')
def threecolumn():
    return render_template("threecolumn.html")


if (__name__) == "__main__":
    app.run(debug=True, port=8080)