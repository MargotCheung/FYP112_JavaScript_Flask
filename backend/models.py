from .extends import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = "user_profile"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    user_coin = db.Column(db.Integer, default=0)
    user_paper_subject = db.Column(db.Integer)
    required_credit_basic = db.Column(db.Integer, default=0)
    complete_credit_basic = db.Column(db.Integer, default=0)
    required_credit_major = db.Column(db.Integer, default=0)
    complete_credit_major = db.Column(db.Integer, default=0)
    required_credit_elec = db.Column(db.Integer, default=0)
    complete_credit_elec = db.Column(db.Integer, default=0)
    required_credit_general	 = db.Column(db.Integer, default=0)
    complete_credit_general	 = db.Column(db.Integer, default=0)
    required_credit_outer = db.Column(db.Integer, default=0)
    complete_credit_outer = db.Column(db.Integer, default=0)
    ability_math = db.Column(db.Float, default=0)
    ability_coding = db.Column(db.Float, default=0)
    ability_logic = db.Column(db.Float, default=0)
    ability_creative = db.Column(db.Float, default=0)
    ability_solve = db.Column(db.Float, default=0)
    join_time = db.Column(db.DateTime, default=datetime.now)

    comments = db.relationship("CommandModel", backref="user")
    paper = db.relationship("PassExamPaperModel", backref="user")
    likes = db.relationship("LikeModel", backref="user")

class CourseInfoModel(db.Model):
    __tablename__ = "course_info"
    # course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(30), nullable=False, primary_key=True)
    course_year = db.Column(db.Integer, nullable=False)
    course_type = db.Column(db.String(30), nullable=False)
    course_credit = db.Column(db.Integer, nullable=False)
    course_intro = db.Column(db.Text)
    math = db.Column(db.Integer, nullable=False)
    coding = db.Column(db.Integer, nullable=False)
    logic = db.Column(db.Integer, nullable=False)
    creative = db.Column(db.Integer, nullable=False)
    solve = db.Column(db.Integer, nullable=False)
    math_txt = db.Column(db.Text)
    coding_txt = db.Column(db.Text)
    logic_txt = db.Column(db.Text)
    creative_txt = db.Column(db.Text)
    solve_txt = db.Column(db.Text)
    # teacher_name = db.Column(db.String(10), nullable=False)

    comments = db.relationship("CommandModel", backref="course")
    teacher = db.relationship("CourseTeacherModel", backref="course")

class CourseTeacherModel(db.Model):
    __tablename__ = "course_teacher"
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(30), db.ForeignKey('course_info.course_name'))
    teacher_name = db.Column(db.String(10), nullable=False)

class CommandModel(db.Model):
    __tablename__ = "lesson_response"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_name = db.Column(db.String(30), db.ForeignKey('course_info.course_name'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'))
    response = db.Column(db.Text)
    comment_time = db.Column(db.DateTime, default=datetime.now)
    
    likes = db.relationship("LikeModel", backref="comment")
#  addgrade = UserGradeModel(course_math=course_math,course_coding=course_coding,course_logic=course_logic,course_creative=course_creative,course_solve=course_solve)
               
class UserGradeModel(db.Model):
    __tablename__ = "user_grades"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'))
    grade = db.Column(db.String(4), nullable=False)
    course_name = db.Column(db.String(30), db.ForeignKey('course_info.course_name'))
    # course_type = db.Column(db.String(30), db.ForeignKey('course_info.course_type'))
    # course_credit = db.Column(db.Integer, db.ForeignKey('course_info.course_credit'))
    score = db.Column(db.Integer, nullable=False)
    course_math = db.Column(db.Float, nullable=False)
    course_coding = db.Column(db.Float, nullable=False)
    course_logic = db.Column(db.Float, nullable=False)
    course_creative = db.Column(db.Float, nullable=False)
    course_solve = db.Column(db.Float, nullable=False)

class PassExamPaperModel(db.Model):
    __tablename__ = "pass_exam_paper"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'))
    teacher = db.Column(db.String(10), nullable=False)
    info = db.Column(db.Text)
    file_data = db.Column(db.LargeBinary, nullable=False)

class LikeModel(db.Model):
    __tablename__ = "likes"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.Integer, db.ForeignKey('user_profile.id'))
    comment_index = db.Column(db.Integer, db.ForeignKey('lesson_response.index'))
    liked_time = db.Column(db.DateTime, default=datetime.now)