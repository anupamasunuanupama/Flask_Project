from flask import *
from database import DB,CR

public=Blueprint("public",__name__)
@public.route("/",methods=["post","get"])
def SignIn():
    if 'submit' in request.form:
        username=request.form['username']
        password=request.form['password']
        
        sql="SELECT * FROM user WHERE username=%s AND password=%s"
        val=(username,password)
        CR.execute(sql,val)
        result=CR.fetchall()
        if result:
            if result[0]['usertype'] == 'doctor':
                return redirect(url_for("doctor.DoctorHome"))
            if result[0]['usertype'] == 'patient':
                return redirect(url_for("patient.PatientHome"))
            return render_template("login.html")
        else:
            flash("Username or password incorrect")
            
    return render_template("login.html")


# @public.route("/register",methods=["post","get"])
# def SignUp():
#     if 'submit' in request.form:
#         name=request.form['name']
#         usertype=request.form['usertype']
#         username=request.form['username']
#         password=request.form['password']
#         email=request.form['email']
        
#         sql="SELECT * FROM user WHERE username=%s OR email=%s"
#         val=(username,email)
#         CR.execute(sql,val)
#         result=CR.fetchall()
        
#         if result:
#             flash("Username or email id already exists")
#         else:
#             sql='INSERT INTO user (name,usertype,username,password,email) VALUES(%s,%s,%s,%s,%s)'
#             val=(name,usertype,username,password,email)
#             CR.execute(sql,val)
#             DB.commit()
#             return render_template("login.html")
        
#     return render_template("register.html")



@public.route("/register",methods=["POST","GET"])
def SignUp():
    if "submit" in request.form:
        print("working-------------------------------------")
        name=request.form['name']
        usertype=request.form['usertype']
        username=request.form['username']
        password=request.form['password']
        email=request.form['email']
        sql='INSERT INTO user (name,usertype,username,password,email) VALUES(%s,%s,%s,%s,%s)'
        val=(name,usertype,username,password,email)
        CR.execute(sql,val)
        DB.commit()
        return redirect(url_for('public.SignIn'))
    
    return render_template('register.html')








@public.route("/logout")
def logout():
    return redirect(url_for("public.SignIn"))