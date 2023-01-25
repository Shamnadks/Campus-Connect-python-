from flask import Flask, render_template, request, redirect, session, jsonify
from DBConnection import Db
import datetime,random


app = Flask(__name__)
app.secret_key="aaaa"

@app.route('/',methods=['get','post'])
def login():
    if request.method=="POST":
        username=request.form['textfield']
        password=request.form['textfield2']
        db=Db()
        res=db.selectOne("select * from login where username='"+username+"' and password='"+password+"'")
        if res:
            type=res['u_type']
            if type=='admin':
                session['lg']='lin'
                return redirect('/home')
            elif type == 'staff':
                session['lid']=res['login_id']
                session['lg'] = 'lin'
                res2=db.selectOne("select * from staff where staff_id='"+str(res['login_id'])+"'")
                session['staff_name']=res2['staff_name']
                session['staff_pic']=res2['profile_pic']
                return redirect('/shome')
            else:
                return '''<script>alert("No such User");window.location="/"</script>'''
        else:
            return '''<script>alert("No such User");window.location="/"</script>'''
    return render_template("loginindex.html")
@app.route('/logout')
def logout():
    session.clear()
    session['lg']=""
    return  redirect('/')


@app.route('/home')
def home():
    if session['lg']=="lin":
        return render_template("Admin/HOME.html")
    else:
        return redirect('/')


@app.route('/staff_add',methods=['get','post'])
def staff_add():
    if session['lg'] == "lin":
        if  request.method=="POST":
            s_name=request.form['textfield']
            phn=request.form['textfield2']
            s_email=request.form['textfield3']
            s_qualification=request.form['textfield4']
            s_adhaar=request.form['textfield5']
            s_profile=request.files['fileField']
            pname=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            s_profile.save(r"C:\\Users\\merin\\PycharmProjects\\university_app\\static\\photo\\"+pname+'.jpg')
            # s_profile.save(r"C:\Users\IDZ\PycharmProjects\university_app\static\photo\\"+pname+'.jpg')
            path="/static/photo/"+pname+'.jpg'
            pswd=request.form['textfield6']
            cpswd=request.form['textfield7']
            db = Db()
            if pswd==cpswd:
                qry=db.selectOne("select * from login WHERE username='"+s_email+"'")
                if qry is not None:
                    return '''<script>alert("Email already exist");window.location="/staff_add"</script>'''
                else:
                    res=db.insert("insert into login values('','"+s_email+"','"+str(pswd)+"','staff')")
                    db.insert("insert into staff values('"+str(res)+"','" + s_name + "','" + phn + "','"+str(path)+"','" + s_email + "','" + s_qualification + "','" + s_adhaar + "')")
                    return '''<script>alert("Success");window.location="/staff_view"</script>'''
            else:
                return '''<script>alert("Password Mismatch");window.location="/staff_add"</script>'''

        else:
            return render_template("Admin/STAFF ADD.html")
    else:
        return redirect('/')

@app.route('/staff_view')
def staff_view():
    if session['lg'] == "lin":
        db=Db()
        ss=db.select("select * from staff")
        return render_template("Admin/STAFF VIEW.html",ab=ss)
    else:
        return redirect('/')

@app.route('/delete_staff/<sid>')
def delete_staff(sid):
    db=Db()
    db.delete("delete from login WHERE login_id='"+sid+"'")
    db.delete("delete from staff WHERE staff_id='"+sid+"'")
    return '''<script>alert("Delete successfully");window.location="/staff_view"</script>'''

@app.route('/staff_edit/<sid>',methods=['get','post'])
def staff_edit(sid):
    if session['lg'] == "lin":
        if request.method == "POST":
            _s_name=request.form['textfield']
            _s_phone=request.form['textfield2']
            _s_email=request.form['textfield3']
            _s_qualification=request.form['textfield4']
            _s_adhaar=request.form['textfield5']
            _s_profile=request.files['fileField']
            pname=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            _s_profile.save(r"C:\Users\merin\PycharmProjects\projectapp\static\photo\\"+pname+'.jpg')
            # _s_profile.save(r"C:\Users\IDZ\PycharmProjects\university_app\static\photo\\"+pname+'.jpg')
            path="/static/photo/"+pname+'.jpg'
            db=Db()
            if request.files!=None:
                if _s_profile.filename!="":
                    db.update("update staff set staff_name='"+_s_name+"',phone_no='"+_s_phone+"',profile_pic='"+str(path)+"',email_id='"+_s_email+"',qualification='"+_s_qualification+"',adhaar_no='"+_s_adhaar+"' where staff_id='"+sid+"'")
                    return '''<script>alert("UPdate successfully");window.location="/staff_view"</script>'''

                else:
                    db.update("update staff set staff_name='"+_s_name+"',phone_no='"+_s_phone+"',email_id='"+_s_email+"',qualification='"+_s_qualification+"',adhaar_no='"+_s_adhaar+"' where staff_id='"+sid+"'")
                    return '''<script>alert("UPdate successfully");window.location="/staff_view"</script>'''

            else:
                db.update( "update staff set staff_name='" + _s_name + "',phone_no='" + _s_phone + "',email_id='" + _s_email + "',qualification='" + _s_qualification + "',adhaar_no='" + _s_adhaar + "' where staff_id='" + sid + "'")
                return '''<script>alert("UPdate successfully");window.location="/staff_view"</script>'''

        else:
            db=Db()
        qry=db.selectOne("select * from staff WHERE staff_id='"+sid+"'")
        return render_template("Admin/STAFF EDIT.html",data=qry)
    else:
        return redirect('/')



@app.route('/doubts_view')
def doubts_view():
    if session['lg'] == "lin":
        db=Db()
        ss=db.select("select * from user,staff,doubts_and_reply where doubts_and_reply.user_id=user.user_id and doubts_and_reply.staff_id=staff.staff_id")
        return render_template("Admin/DOUBT&REPLY VIEW.html",data=ss)
    else:
        return redirect('/')

@app.route('/course_add',methods=['get','post'])
def course_add():
    if session['lg'] == "lin":
        if request.method=="POST":
            deptid=request.form['s']
            course=request.form['textfield']
            db=Db()
            qry=db.selectOne("select * from course WHERE department_id='"+deptid+"' and course='"+course+"'")
            if qry is not None:
                return '''<script>alert("already added");window.location="/course_add"</script>'''
            else:
                db.insert("insert into course VALUES ('','"+deptid+"','"+course+"')")
                return '''<script>alert("Success");window.location="/course_view"</script>'''
        else:
            db=Db()
            res=db.select("select * from department")
            return render_template("Admin/COURSE ADD.html",data=res)
    else:
        return redirect('/')

# @app.route('/course_edit',methods=['get','post'])
# def course_edit():
#     if request.method=="POST":
#         _course=request.form['textfield']
#     return render_template("Admin/COURSE EDIT.html")
#
@app.route('/course_view')
def course_view():
    if session['lg'] == "lin":
        db=Db()
        ss=db.select("select * from course,department WHERE department.department_id=course.department_id")
        return render_template("Admin/COURSE VIEW.html",data=ss)
    else:
        return redirect('/')

@app.route('/delete_course/<cid>')
def delete_course(cid):
    db=Db()
    db.delete("delete  from course WHERE course_id='"+cid+"'")
    return '''<script>alert("success");window.location="/course_view"</script>'''


@app.route('/department_add',methods=['get','post'])
def department_add():
    if session['lg'] == "lin":
        if request.method=="POST":
            dept_name=request.form['textfield']
            db=Db()
            qry=db.selectOne("select * from department WHERE department_name='"+dept_name+"'")
            if qry is not None:
                return '''<script>alert("Already addedd");window.location="/department_add"</script>'''
            else:
                db.insert("insert into department values('','"+dept_name+"')")
                return '''<script>alert("Success");window.location="/department_view"</script>'''
        else:
            return render_template("Admin/DEPT ADD.html")
    else:
        return redirect('/')

# @app.route('/department_edit',methods=['get','post'])
# def department_edit():
#     if request.method=="POST":
#         dept_name=request.form['textfield']
#     return render_template("Admin/DEPT EDIT.html")

@app.route('/department_view')
def department_view():
    if session['lg'] == "lin":
        db=Db()
        ss=db.select("select * from department")
        return render_template("Admin/DEPTVIEW.html",data=ss)
    else:
        return redirect('/')

@app.route('/delete_dept/<did>')
def delete_dept(did):
    db=Db()
    db.delete("delete from department WHERE department_id='"+did+"'")
    return '''<script>alert("Success");window.location="/department_view"</script>'''


@app.route('/previous_question_papers_view')
def previous_question_papers_view():
    if session['lg'] == "lin":
        db=Db()
        ss=db.select("select * from previous_questions,subject where previous_questions.subjecct_id=subjecct.subject_id")
        return render_template("Admin/PRVS_QSTN VIEW.html",data=ss)
    else:
        return redirect('/')





@app.route('/subject_add',methods=['get','post'])
def subject_add():
    if session['lg'] == "lin":
        if request.method == "POST":
            course=request.form['s']
            subject=request.form['textfield']
            semester=request.form['sem']
            db=Db()
            qry=db.selectOne("select * from subject where course_id='"+course+"' and subject='"+subject+"'and semester='"+semester+"'")
            if qry is not None:
                return '''<script>alert("already added");window.location="/subject_add"</script>'''
            else:
                db.insert("insert into subject values('','"+subject+"','"+course+"','"+semester+"')")
                return '''<script>alert("Success");window.location="/subject_view"</script>'''
        else:
            db=Db()
            res=db.select("select * from course")
            return render_template("Admin/SUB ADD.html",data=res)
    else:
        return redirect('/')


@app.route('/subject_view')
def subject_view():
    if session['lg'] == "lin":
        db=Db()
        ss=db.select("select * from subject,course where subject.course_id=course.course_id")
        return render_template("Admin/SUB VIEW.html",data=ss)
    else:
        return redirect('/')

@app.route('/delete_subject/<suid>')
def delete_subject(suid):
    db=Db()
    db.delete("delete from subject WHERE subject_id='"+suid+"'")
    return '''<script>alert("Success");window.location="/subject_view"</script>'''


@app.route('/suballoc_add',methods=['get','post'])
def suballoc_add():
    if session['lg'] == "lin":
        if request.method=="POST":
            subject=request.form['select']
            staff=request.form['select2']
            db=Db()
            db.insert("insert into suballoc values('','"+subject+"','"+staff+"')")

            return '''<script>alert("Success");window.location="/suballoc_view"</script>'''
        else:
            db=Db()
            qry=db.select("select * from staff")
            qry2=db.select("select * from subject")

            return render_template("Admin/SUBALLOC ADD.html",data=qry2,data1=qry)
    else:
        return redirect('/')

# @app.route('/suballoc_edit',methods=['get','post'])
# def suballoc_edit():
#     if request.method=="POST":
#         _subject_name=request.form['select']
#         _staff=request.form['select2']
#     return render_template("Admin/SUBALLOC EDIT.html")

@app.route('/suballoc_view')
def suballoc_view():
    if session['lg'] == "lin":
                db=Db()
                ss=db.select("select * from staff,subject,suballoc where suballoc.subject_id=subject.subject_id and suballoc.staff_id=staff.staff_id")
                return render_template("Admin/SUBALLOC VIEW.html",data=ss)
    else:
        return redirect('/')

@app.route('/delete_allocation/<aid>')
def delete_allocation(aid):
    db=Db()
    db.delete("delete from suballoc WHERE suballoc_id='"+aid+"'")
    return '''<script>alert("Success");window.location="/suballoc_view"</script>'''


# @app.route('/user_add',methods=['get','post'])
# def user_add():
#     if request.method=="POST":
#         u_name=request.form['textfield']
#         u_adhaar=request.form['textfield2']
#         u_profile=request.form['fileField']
#         u_email=request.form['textfield4']
#         u_phone= request.form['textfield5']
#     return render_template("Admin/USER ADD.html")


@app.route('/user_view')
def user_view():
    if session['lg'] == "lin":
        db=Db()
        ss=db.select("select * from user")
        return render_template("Admin/USER VIEW.html",data=ss)
    else:
        return redirect('/')


@app.route('/suggestion_view')
def suggestion_view():
    if session['lg'] == "lin":
        db=Db()
        ss=db.select("select * from suggestion,user where suggestion.user_id=user.user_id")
        return render_template("Admin/SUGGESTION_VIEW.html",data=ss)
    else:
        return redirect('/')

@app.route('/view_prev_qp')
def view_prev_qp():
    if session['lg'] == "lin":
        db=Db()
        ss=db.select("select * from previous_questions,subject,course where previous_questions.subject_id=subject.subject_id and subject.course_id=course.course_id")
        return render_template("Admin/view_previous_question_papers.html",data=ss)
    else:
        return redirect('/')


# --------------------------------------------------------------------------------------------------------------------------------------------------
#                                                            STAFF MODULE
# ------------------------------------------------------------------------------------------------------------------------------------------------------



@app.route('/sreply/<id>',methods=['get','post'])
def sreply(id):
    if session['lg'] == "lin":
        if request.method=="POST":
            r=request.form['textarea']
            db=Db()
            db.update("update doubts_and_reply set reply='"+r+"',r_date=curdate() where doubt_id='"+id+"'")
            return '''<script>alert("Success");window.location="/shome"</script>'''
        return render_template("Staff/reply.html")
    else:
        return redirect('/')

@app.route('/shome')
def shome():
    if session['lg'] == "lin":
        return render_template("Staff/SHOME.html")
    else:
        return redirect('/')

@app.route('/up_focus',methods=['get','post'])
def up_focus():
    if session['lg'] == "lin":
        db = Db()
        if request.method=="POST":
            sub=request.form['select2']
            syllabus=request.form['textarea']
            file=request.files['fileField']
            fname = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            file.save(r"C:\\Users\\merin\\PycharmProjects\\university_app\\static\\pdf\\" + fname + '.pdf')
            path = "/static/pdf/" + fname + '.pdf'
            res = db.insert("insert into focus_area values('','"+str(sub)+"','" + syllabus + "','"+str(path)+"')")
            return '''<script>alert("Success");window.location="/shome"</script>'''
        else:
            rs = db.select("select * from subject,suballoc where suballoc.subject_id=subject.subject_id and suballoc.staff_id='" + str(session['lid']) + "'")
            return render_template("Staff/upload_focusarea.html",data=rs)
    else:
        return redirect('/')

@app.route('/up_note',methods=['get','post'])
def up_not2e():
    if session['lg'] == "lin":
         db=Db()
         if request.method=="POST":
             sub=request.form['select2']
             note=request.files['fileField']
             fname = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
             note.save(r"C:\\Users\\merin\\PycharmProjects\\university_app\\static\\pdf\\" + fname + '.pdf')
             path = "/static/pdf/" + fname + '.pdf'
             res=db.insert("insert into note values('','"+sub+"','"+str(path)+"',curdate())")
             return '''<script>alert("Success");window.location="/shome"</script>'''
         else:
             rs=db.select("select * from subject,suballoc where suballoc.subject_id=subject.subject_id and suballoc.staff_id='"+str(session['lid'])+"'")
             return render_template("Staff/upload_note.html",data=rs)
    else:
        return redirect('/')

@app.route('/up_prev',methods=['get','post'])
def up_prev():
    if session['lg'] == "lin":
        db=Db()
        if request.method=="POST":
            year=request.form['textfield']
            sub=request.form['select2']
            qp=request.files['fileField']
            qp_name=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            qp.save(r"C:\\Users\\merin\\PycharmProjects\\university_app\\static\\pdf\\" + qp_name + '.pdf')
            path = "/static/pdf/" + qp_name + '.pdf'
            res=db.insert("insert into previous_questions values('','"+year+"','"+str(path)+"','"+sub+"')")
            return '''<script>alert("Success");window.location="/shome"</script>'''
        else:
            rs = db.select("select * from subject,suballoc where suballoc.subject_id=subject.subject_id and suballoc.staff_id='" + str(session['lid']) + "'")
            return render_template("Staff/upload_prev_qp.html",data=rs)
    else:
        return redirect('/')

@app.route('/up_video',methods=['get','post'])
def up_video():
    if session['lg'] == "lin":
        db = Db()
        if request.method=="POST":
            sub=request.form['select2']
            video=request.files['fileField']
            vname=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            video.save(r"C:\Users\merin\PycharmProjects\university_app\static\video\\" + vname + '.mp4')
            path = "/static/video/" + vname + '.mp4'
            res=db.insert("insert into video values('','"+sub+"','"+str(path)+"',curdate())")
            return '''<script>alert("Success");window.location="/shome"</script>'''
        else:
            rs = db.select("select * from subject,suballoc where suballoc.subject_id=subject.subject_id and suballoc.staff_id='" + str(session['lid']) + "'")
            return render_template("Staff/upload_video.html",data=rs)
    else:
             return redirect('/')

@app.route('/v_dbt')
def v_dbt():
    if session['lg'] == "lin":
        db=Db()
        res=db.select("select * from doubts_and_reply,user where doubts_and_reply.staff_id='"+str(session['lid'])+"' and doubts_and_reply.user_id=user.user_id")
        return render_template("Staff/view_dbt.html",data=res)
    else:
        return redirect('/')


@app.route('/v_focus/<id>')
def v_focus(id):
    if session['lg'] == "lin":
        db=Db()
        sid=session['lid']
        print(sid)
        res=db.select("select * from focus_area where subject_id='"+str(id)+"'")
        print(res)
        return render_template("Staff/view_focusarea.html",data=res)
    else:
        return redirect('/')

@app.route('/v_note/<id>')
def v_note(id):
    if session['lg'] == "lin":
        db=Db()
        res=db.select("select * from note where subject_id='"+id+"'")
        return render_template("Staff/view_notes.html",data=res)
    else:
        return redirect('/')


@app.route('/v_pqr/<id>')
def v_pqr(id):
    if session['lg'] == "lin":
        db=Db()
        res=db.select("select * from previous_questions  where subject_id='"+id+"'")
        return render_template("Staff/view_pqr.html",data=res)
    else:
        return redirect('/')


@app.route('/v_profile')
def v_profile():
    if session['lg'] == "lin":
        db=Db()
        res=db.selectOne("select * from staff where staff_id='"+str(session['lid'])+"'")
        return render_template("Staff/View_profile.html",data=res)
    else:
        return redirect('/')

@app.route('/v_rating')
def v_rating():
    if session['lg'] == "lin":
        db=Db()
        res=db.select("select * from rating,staff,user where rating.staff_id=staff.staff_id and rating.user_id=user.user_id and rating.staff_id='"+str(session['lid'])+"'")
        return render_template("Staff/view_ratingd.html",data=res)
    else:
        return redirect('/')

@app.route('/v_suballoc')
def v_suballoc():
    if session['lg'] == "lin":
        db=Db()
        res=db.select("select * from suballoc,subject,staff where suballoc.subject_id=subject.subject_id and suballoc.staff_id=staff.staff_id and suballoc.staff_id='"+str(session['lid'])+"'")
        return render_template("Staff/view_sub_alloc.html",data=res)
    else:
        return redirect('/')


@app.route('/v_sugg')
def v_sugg():
    if session['lg'] == "lin":
        db=Db()
        res=db.select("select * from suggestion,user where suggestion.user_id=user.user_id and suggestion.staff_id='"+str(session['lid'])+"'")
        return render_template("Staff/view_suggestions.html",data=res)
    else:
        return redirect('/')

@app.route('/v_video/<id>')
def v_video(id):
    if session['lg'] == "lin":
       db=Db()
       res=db.select("select * from video where subject_id='"+id+"'")
       return render_template("Staff/view_video.html",data=res)
    else:
        return redirect('/')





# ------------------------------------------------------------------------android----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/and_login',methods=['post'])
def and_login():
    uname = request.form['u']
    pswd = request.form['p']
    db=Db()
    res = db.selectOne("select * from login where username='" + uname + "' and password='" + pswd + "'")
    print(res)
    return jsonify(status='ok',lid=res['login_id'],type=res['u_type'],data=res)


# if res is not None:
#     ss = {}
#     ss['status'] = "ok"
#     ss['type'] = res['u_type']
#     ss['lid'] = res['login_id']
#     ss['data'] = res
#     return demjson.encode(ss)
# else:
#     ss = {}
#     ss['status'] = "none"
#     return demjson.encode(ss)


@app.route('/and_registeration')
def and_registeration():
    uname = request.form['na']
    email = request.form['em']
    phn=request.form['phon']
    inst = request.form['insti']
    course = request.form['co']
    prgm = request.form['dep']
    batch = request.form['batch']
    aadhar = request.form['adar']
    password = request.form['p']
    confirm= request.form['cnfp']
    print(uname,email,phn,inst,course,prgm,batch,aadhar,password,confirm)
    db=Db()
    s=db.insert("insert into login VALUES ('','"+email+"','"+password+"','user')")
    db.insert("insert into user VALUES ('','"+uname+"','"+aadhar+"','','"+email+"','"+phn+"','"+course+"','"+batch+"','"+inst+"')")

    return jsonify(status = "ok")

@app.route('/and_send_doubt',methods=['post'])
def and_send_doubt():

    u_id = request.form['id']
    doubt = request.form['doubt']
    sub = request.form['sub']
    print(doubt,u_id)
    db=Db()
    ss=db.insert("insert into doubts_and_reply VALUES ('','"+doubt+"','pending',curdate(),'pending','"+u_id+"','"+str(sub)+"')")
    return jsonify(status="ok",data=ss)

@app.route('/and_send_rating',methods=['post'])
def and_send_rating():
    u_id = request.form['id']
    rating = request.form['rat']
    sub = request.form['sub']
    db = Db()
    s1 = db.selectOne("select * from suballoc where subject_id='" + str(sub) + "' ")
    if s1 is not None:
        sid = s1['staff_id']
        ss=db.insert("insert into rating VALUES ('','"+str(sid)+"','"+u_id+"','"+rating+"',curdate())")
        return jsonify(status="ok",data=ss)
    else:
        return jsonify(status="none")
@app.route('/view_statusdd',methods=['post'])
def view_statusdd():
    u_id = request.form['id']

    sub = request.form['sub']
    db = Db()
    s1=db.selectOne("select * from suballoc where subject_id='"+str(sub)+"' ")
    if s1 is not None:
        sid=s1['staff_id']
        ss = db.select("select * from doubts_and_reply where staff_id='" + str(sid) + "' and user_id='"+u_id+"' ")
        return jsonify(status="ok",data=ss)
    else:
        return jsonify(status="none")


@app.route('/send_suggestion',methods=['post'])
def send_suggestion():
    u_id = request.form['id']
    sugtion = request.form['sug']
    sub = request.form['sub']
    db = Db()
    s1=db.selectOne("select * from suballoc where subject_id='"+str(sub)+"' ")
    if s1 is not None:
        sid=s1['staff_id']
        db.insert("insert into suggestion VALUES ('','"+sugtion+"','"+u_id+"','"+str(sid)+"')")
        return jsonify(status="ok")
    else:
        return jsonify(status="none")



@app.route('/viewprofile',methods=['post'])
def viewprofile():

    u_id = request.form['login_id']
    print(u_id)
    db=Db()
    ss=db.selectOne("select * from user,course where user_id='"+str(u_id)+"' and course.course_id=user.course")
    print(ss)
    return jsonify(status="ok",data=ss)




@app.route('/and_view_pqs',methods=['post'])
def and_view_pqs():

    u_id = request.form['id']
    sub = request.form['sub']
    print(u_id)
    db=Db()
    ss=db.select("select * from previous_questions where subject_id='"+str(sub)+"' ")
    return jsonify(status="ok",data=ss)




@app.route('/and_view_notes',methods=['post'])
def and_view_notes():

    u_id = request.form['id']
    sub = request.form['sub']
    print(u_id)
    db = Db()
    ss=db.select("select * from user,course,note,subject where user.course=course.course_id and  note.subject_id=subject.subject_id and  note.subject_id='"+str(sub)+"' and  user.user_id='"+str(u_id)+"'")
    print(ss)
    return jsonify(status="ok",data=ss)




@app.route('/and_view_subject',methods=['post'])
def and_view_subject():

    u_id = request.form['id']
    print(u_id)
    db=Db()
    ss=db.select("select * from suballoc,subject,staff,user where suballoc.staff_id=staff.staff_id and suballoc.subject_id=subject.subject_id and user.course=subject.course_id and user.user_id='"+str(u_id)+"'")
    print(ss)
    return jsonify(status="ok",data=ss)

@app.route('/and_focus',methods=['post'])
def and_focus():

    u_id = request.form['id']
    sub = request.form['sub']
    print(u_id)
    db = Db()
    ss=db.select("select * from user,course,focus_area where user.course=course.course_id and  focus_area.subject_id='"+str(sub)+"' and  user.user_id='"+str(u_id)+"'")
    print(ss)
    return jsonify(status="ok",data=ss)
if __name__ == '__main__':
    app.run(host="0.0.0.0")
