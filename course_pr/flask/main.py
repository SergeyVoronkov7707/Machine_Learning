import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import dill



# Create flask app
flask_app = Flask(__name__)

with open('Voronkov_pipeline_model.dill', 'rb') as in_strm:
    model = dill.load(in_strm)

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    try:
        float_features = [ x for x in request.form.values()]

        features = pd.DataFrame(np.array(float_features).reshape((1,-1)), columns=['date', 'countryregion', 'deaths', 'recovered', 'active'])
        prediction = model.predict(features)

        tran_tab = str.maketrans(
            dict.fromkeys(list("\n ,|, . a-  # @ ! $ % ^ & * = ] [ \'  \" < > ~  ) ( № ; : ? +  / -"), ""))
        float_ = float_features[0].translate(tran_tab)

        return render_template("index.html", prediction_text = f"Подтвержденных на дату {float_} : {round(prediction[0])}")
    except:
        return render_template('index.html', prediction_text= 'нужно заполнить все 5 полей верно!')

if __name__ == "__main__":
    flask_app.run(host= '0.0.0.0',port= 3000, debug=True)