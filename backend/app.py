from flask import Flask
from flask import jsonify,request
from path import Path
from backend.db import cursor, connection
from flask import Flask, session, g
from flask import jsonify
from path import Path
from . import config
from .extends import db

from .models import UserModel

from .blueprints.course import bp as course_bp
from .blueprints.auth import bp as auth_bp

from flask_migrate import Migrate

from .views.home import home_view
# from .views.lesson import lessonpage_view
from .views.learningProgress import learningProgress_view, profileDroplist_view
from .views.profile import profile_view
from .views.CoinWallet import CoinWallet_view
from .views.landing import landing_view
from .views.lessonPage import lessonPage_view, get_lesson_name
from .views.MyQuestionBank import MyQuestionBank_view
from .views.lessonDiscussion import lessonDiscussion_view, liked_view
from .views.signIn import signIn_view


PROJECT_DIR = Path(__file__).parent.parent
FRONTEND_DIR = PROJECT_DIR / 'backend'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

# 綁定配置文件
app.config.from_object(config)

# 初始化
db.init_app(app)

migrate = Migrate(app, db)

# 每一個blueprints都用這樣寫
app.register_blueprint(course_bp)
app.register_blueprint(auth_bp)

@app.route('/profile')
def profile():
    return profile_view()

@app.route("/learningProgress", methods=["GET", "POST"])
def learningProgress():
    return learningProgress_view()

# @app.route("/saveData/<course_name>", methods=["POST"])
# def saveData(course_name):
#     return save_data(course_name)

@app.route("/profileDroplist/<course_year>")
def profileDroplist(course_year):
    return profileDroplist_view(course_year)

@app.route("/CoinWallet")
def CoinWallet():
    return CoinWallet_view()

@app.route("/landing")
def landing():
    return landing_view()

@app.route("/lessonPage", methods=["GET", "POST"])
def lessonPage():
    return lessonPage_view()

@app.route('/lessonName', methods=['GET'])
def lessonNameApi():
    return get_lesson_name()    

@app.route("/MyQuestionBank")
def MyQuestionBank():
    return MyQuestionBank_view()

@app.route("/lessonDiscussion/course_name=<course_name>",methods=["GET", "POST"])
def lessonDiscussion(course_name):
    return lessonDiscussion_view(course_name)

@app.route("/like-comment/course_name=<course_name>/<comment_index>",methods=["GET", "POST"])
def likedFunction(course_name,comment_index):
    return liked_view(course_name,comment_index)

# hook函數 （具體有點難解釋，可以去找一下相關内容）
@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)

# 這個是在templete裏呼叫，以達到登入后用戶名可以顯示
@app.context_processor
def my_context_processor():
    return {"user": g.user}

if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/")
# def home():
#     return home_view()

# @app.route("/lesson/<row_course_name>")
# def lesson(row_course_name):
#     return lessonpage_view(row_course_name)

