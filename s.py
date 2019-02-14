from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request:
        print(request.form)
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
