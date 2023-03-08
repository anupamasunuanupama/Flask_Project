from flask import *
from database import DB,CR

doctor=Blueprint("doctor",__name__)
@doctor.route("/")
def DoctorHome():
    return render_template("doctorhome.html")
@doctor.route("/answerquestion",methods=["post","get"])
def AnswerQuestion():
    CR.execute("SELECT * FROM qanda")
    qanda=CR.fetchall()
    if 'submit' in request.form:
        answer=request.form['ans']
        id=request.form['submit']
        sql="UPDATE qanda set answer=%s WHERE id=%s"
        val=(answer,id)
        CR.execute(sql,val)
        DB.commit()
        flash("Answer Submitted")
        return redirect(url_for("doctor.AnswerQuestion"))
    
    return render_template("answerquestion.html",qanda=qanda)

@doctor.route("/delete",methods=["post","get"])
def delete():
    CR.execute("SELECT * FROM qanda"),
    res=CR.fetchall()
    if 'submit' in request.form:
        id=request.form['submit']
        CR.execute("DELETE FROM qanda WHERE id=%s",(id,))
        DB.commit()
  
        flash("Item Delete")
        return redirect(url_for('doctor.delete'))
    return render_template("delete.html",res=res)    
    