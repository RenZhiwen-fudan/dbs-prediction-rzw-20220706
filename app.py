from flask import Flask
from flask import request, render_template
import joblib
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model = joblib.load("Regression")
        r = model.predict([[rates]])
        return(render_template("index.html", result=r))
    else:
        return(render_template("index.html", result="WAITING"))
if __name__=="__main__":
    app.run()