from flask import Flask
from flask import jsonify,request
from path import Path
from backend.db import cursor, connection

from .views.home import home_view
from .views.lesson import lessonpage_view
from .views.learningProgress import learningProgress_view, save_data
from .views.profile import profile_view
from .views.CoinWallet import CoinWallet_view
from .views.landing import landing_view
from .views.lessonPage import lessonPage_view, get_lesson_name
from .views.MyQuestionBank import MyQuestionBank_view
from .views.lessonDiscussion import lessonDiscussion_view


PROJECT_DIR = Path(__file__).parent.parent
FRONTEND_DIR = PROJECT_DIR / 'backend'
app = Flask(__name__)


@app.route('/profile')
def profile():
    return profile_view()

@app.route("/learningProgress/<user_id>")
def learningProgress(user_id):
    return learningProgress_view(user_id)

@app.route("/saveData", methods=["POST"])
def save_data():
    data = request.form  # 接收前端发送的JSON数据
    print(data)
    # save_data(data)  # 调用save_data()函数来保存数据
    user_id="007"  
    grade = data.get('grade')
    course_name = data.get('course_name')
    course_type = data.get('course_type')
    course_credit = data.get('course_credit')
    score = data.get('score')

    sql_query = f'INSERT INTO user_grades (user_id, grade, course_name, course_type, course_credit, score) VALUES ("{user_id}","{grade}", "{course_name}","{course_type}","{course_credit}","{score}")'
    # values = (grade, subject, category, credits, score)
    cursor.execute(sql_query)
    connection.commit()
    return jsonify({"message": "Data saved successfully"})

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

@app.route("/lessonDiscussion",methods=["GET", "POST"])
def lessonDiscussion():
    return lessonDiscussion_view()



if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/")
# def home():
#     return home_view()

# @app.route("/lesson/<row_course_name>")
# def lesson(row_course_name):
#     return lessonpage_view(row_course_name)

