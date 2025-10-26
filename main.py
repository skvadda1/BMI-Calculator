from flask import Flask, render_template, request 
from datetime import datetime
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/calculate", methods=["POST"])
def calculate_bmi():                                        
    try:
        Weight = float(request.form.get("Weight(lbs)"))
        Height = float(request.form.get("Height(in)"))
        BMI = (Weight/(Height ** 2)) * 703
        return render_template("index.html", BMI=BMI)
    except ValueError:
        return render_template("index.html", error="Please enter a valid number.")
if __name__ == "__main__":
    app.run(debug=True)