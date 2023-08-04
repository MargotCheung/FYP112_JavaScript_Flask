from flask import Blueprint, render_template, request
from models import CourseInfoModel
# from flask_sqlalchemy import Article

bp = Blueprint("course", __name__, url_prefix="/")

@bp.route('/')
def homePage():
    return render_template("homepage.html")

@bp.route('/searchResult',methods=['GET', 'POST'])
def searchResult():
    if request.method == 'GET':
        # page = request.args.get('page', 1)
        # articles = Article.query.paginate()
        # course_list = CourseInfoModel.query.order_by(CourseInfoModel.id).all()
        return render_template("search_result.html", course_list=course_list)