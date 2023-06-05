from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Defining the homepage of our site

@app.route("/") # this sets the route to this page
def home():
	return render_template("index.html", content=["Testing"])

@app.route("/test") # this sets the route to this page
def test():
	return render_template("new.html")


if __name__ == "__main__":
	app.run(debug=True)

