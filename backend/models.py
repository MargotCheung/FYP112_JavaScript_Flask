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
    required_credit_basic = db.Column(db.Integer)
    complete_credit_basic = db.Column(db.Integer)
    required_credit_major = db.Column(db.Integer)
    complete_credit_major = db.Column(db.Integer)
    required_credit_elec = db.Column(db.Integer)
    complete_credit_elec = db.Column(db.Integer)
    required_credit_general	 = db.Column(db.Integer)
    complete_credit_general	 = db.Column(db.Integer)
    required_credit_outer = db.Column(db.Integer)
    complete_credit_outer = db.Column(db.Integer)
    ability_math = db.Column(db.Float, default=0)
    ability_coding = db.Column(db.Float, default=0)
    ability_logic = db.Column(db.Float, default=0)
    ability_creative = db.Column(db.Float, default=0)
    ability_solve = db.Column(db.Float, default=0)
    join_time = db.Column(db.DateTime, default=datetime.now)

    commands = db.relationship("CommandModel", back_populates="user")

class CourseInfoModel(db.Model):
    __tablename__ = "course_info"
    course_id = db.Column(db.Integer, primary_key=True)
    course_year = db.Column(db.Integer, nullable=False)
    course_name = db.Column(db.String(30), nullable=False)
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
    teacher_name = db.Column(db.String(10), nullable=False)

    commands = db.relationship("CommandModel", back_populates="course")

class CommandModel(db.Model):
    __tablename__ = "lesson_response"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course_info.course_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'))
    response = db.Column(db.Text)
    command_time = db.Column(db.DateTime, default=datetime.now)
    liked = db.Column(db.Integer, default=0)

    course = db.relationship("CourseInfoModel", back_populates="commands")
    user = db.relationship("UserModel", back_populates="commands")

class UserGradeModel(db.Model):
    __tablename__ = "user_grades"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'))
    grade = db.Column(db.String(4), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course_info.course_id'))
    # course_type = db.Column(db.String(30), db.ForeignKey('course_info.course_type'))
    # course_credit = db.Column(db.Integer, db.ForeignKey('course_info.course_credit'))
    score = db.Column(db.Integer, nullable=False)