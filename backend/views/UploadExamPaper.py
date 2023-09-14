from flask import render_template, url_for, request, jsonify, g, redirect, flash
from ..models import CourseInfoModel, UserModel, PassExamPaperModel, CourseTeacherModel
from ..extends import db
from ..blueprints.form import UploadPaperForm

def UploadExamPaper_view():
    user_id = g.user.id
    form = UploadPaperForm(request.form)
    if request.method == "POST":
        file = request.files['file']
        year = form.year.data
        course = form.course.data
        teacher = form.teacher.data
        # file = form.pdf_file.data
        # filename = file.filename
        # file_data = file.read()
        info = form.info.data
        
        upload_pdf = PassExamPaperModel(year=year, course=course, user_id=user_id, teacher=teacher, info=info, file_data=file.read())
        db.session.add(upload_pdf)
        db.session.commit()
    else:
        return render_template("uploadPaper.html", form=form)
    return render_template("uploadPaper.html", form=form)