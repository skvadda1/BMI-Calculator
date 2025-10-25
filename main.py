from flask import Flask, render_template, request 
from datetime import datetime
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/calculate", methods=["POST"])
def calculate_leap_year():
    try:
        leap_year = int(request.form.get("year"))
        if leap_year % 4 == 0:
            return render_template("index.html", year=" a leap year")
        else:
            return render_template("index.html", year=" not a leap year")
    except ValueError:
        return render_template("index.html", error="Please enter a valid number.")
if __name__ == "__main__":
    app.run(debug=True)