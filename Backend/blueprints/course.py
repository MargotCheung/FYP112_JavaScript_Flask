from flask import Blueprint, render_template, request

bp = Blueprint("course", __name__, url_prefix="/")

@bp.route('/')
def homePage():
    return render_template("homepage.html")

@bp.route('/searchResult',methods=['GET', 'POST'])
def searchResult():
    if request.method == 'GET':
        return render_template("search_result.html")