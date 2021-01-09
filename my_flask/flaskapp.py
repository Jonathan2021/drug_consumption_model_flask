from flask import Flask, render_template, request
import joblib
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html")
@app.route("/form")
def form():
    return render_template("form.html")
@app.route("/result",methods=["POST"])
def result():
    age=request.form.get("age")
    gender=request.form.get("gender")
    education=request.form.get("education")
    ethnicity=request.form.get("ethnicity")
    neuroticism=request.form.get("neuroticism")
    extraversion=request.form.get("extraversion")
    opennesstoexperience=request.form.get("opennesstoexperience")
    agreeableness=request.form.get("agreeableness")
    conscientiousness=request.form.get("conscientiousness")
    impulsiveness=request.form.get("impulsiveness")
    sensationseeking=request.form.get("sensationseeking")
    ##ici faire la traduction de string vers int pour fit le modele
    try:
        age=int(age)
    except:
        error_statement= "enter your age with integers.."
        return render_template("/form.html",
         error_statement=error_statement,
          age=age,
          gender=gender,
          education=education,
          ethnicity=ethnicity,
          neuroticism=neuroticism,
          extraversion=extraversion,
          opennesstoexperience=opennesstoexperience,
          agreeableness=agreeableness,
          conscientiousness=conscientiousness,
          impulsiveness=impulsiveness,
          sensationseeking=sensationseeking)
    features_list=[age, gender,education,ethnicity,neuroticism,extraversion,opennesstoexperience,agreeableness,conscientiousness,impulsiveness,sensationseeking]
    model=joblib.load("model.joblib")
    prediction=model.predict(features_list)
    return render_template("result.html",prediction)


if __name__ == "__main__":
    app.run()
