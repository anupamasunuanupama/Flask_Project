from flask import Flask
from flask import *
from public import public
from patient import patient
from doctor import doctor

app=Flask(__name__)
app.secret_key="zion"
# @app.route("/")
# def Home():
#     return render_template("login.html")

app.register_blueprint(public)
app.register_blueprint(patient,url_prefix="/patient")
app.register_blueprint(doctor,url_prefix="/doctor")
app.run(debug=True,port=5010)