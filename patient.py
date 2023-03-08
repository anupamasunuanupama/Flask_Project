from flask import *
from database import DB,CR
from datetime import datetime

patient =Blueprint("patient",__name__)

@patient.route("/")
def PatientHome():
    CR.execute("SELECT * FROM qanda")
    res=CR.fetchall()
    return render_template("patienthome.html",res = res)

@patient.route("/askquestion",methods=["post","get"])
def Askquestion():
    if 'submit' in request.form:
        question =request.form['question']
        date=datetime.now()
        sql='INSERT INTO qanda (question,date) VALUES(%s,%s)'
        val=(question,date)
        CR.execute(sql,val)
        DB.commit()
        flash("Question submitted")
        return redirect(url_for('patient.PatientHome'))
    
    return render_template("askquestion.html")