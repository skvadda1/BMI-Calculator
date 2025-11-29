from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate_bmi():
    try:
        weight = float(request.form.get("Weight(lbs)"))
        height = float(request.form.get("Height(in)"))
        bmi = (weight / (height ** 2)) * 703
        if 9 <= bmi <= 18:
            message = "You are underweight"
        elif 19 <= bmi <= 24:
            message = "You are healthy"
        elif 25 <= bmi <= 29:
            message = "You are overweight"
        elif 30 <= bmi <= 39:
            message = "You are obese"
        elif 40 <= bmi > 65:
            message = "You are EXTREMELY obese"
        else:
            message = "BMI is out of expected range"
        return render_template("index.html", BMI=bmi, message=message)

    except ValueError:
        return render_template("index.html", error="Please enter a valid number.")

if __name__ == "__main__":
    app.run(debug=True)
