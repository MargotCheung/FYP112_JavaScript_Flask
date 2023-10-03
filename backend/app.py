from flask import Flask
from flask import jsonify,request
from path import Path
from backend.db import cursor, connection
from flask import Flask, session, g
from flask import jsonify
from path import Path
from . import config
from .extends import db

from .models import UserModel, CourseInfoModel

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
from .views.UploadExamPaper import UploadExamPaper_view

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

@app.route("/UploadExamPaper", methods=["GET", "POST"])
def UploadExamPaper():
    return UploadExamPaper_view()

# @app.route('/updateCourse', methods=["GET", "POST"])
# def update_users():
#     # Get the data you want to update from the request or any other source.
#     updated_data = [
#         {'name': '計算機概論', 
#         'math': 0.30,
#         'coding': 0.30,       
#         'logic': 0.90,        
#         'creative': 0.30,     
#         'solve': 0.90
#         },
#         {'name': '程式設計(I)',
#         'math': 0.30,
#         'coding': 0.90,       
#         'logic': 0.90,        
#         'creative': 0.30,     
#         'solve': 0.90
#         },
#         {'name': '程式設計(II)',
#         'math': 0.60,
#         'coding': 1.20,
#         'logic': 0.90,
#         'creative': 0.60,
#         'solve': 0.90
#         },
#         {'name': '普通物理-電、磁、光',
#         'math': 0.90,
#         'coding': 0.00,
#         'logic': 0.90,
#         'creative': 0.30,
#         'solve': 1.20
#         },
#         {'name': '微積分(一)',
#         'math': 0.90,
#         'coding': 0.00,
#         'logic': 0.90,
#         'creative': 0.60,
#         'solve': 1.20
#         },
#         {'name': '微積分(一)實習',
#         'math': 0.90,
#         'coding': 0.00,
#         'logic': 0.90,
#         'creative': 0.60,
#         'solve': 1.20
#         },
#         {'name': '程式設計(III)',
#         'math': 0.60,
#         'coding': 1.20,
#         'logic': 0.90,
#         'creative': 0.60,
#         'solve': 0.90
#         },
#         {'name': '程式設計(IV)',
#         'math': 0.60,
#         'coding': 1.20,
#         'logic': 0.90,
#         'creative': 0.60,
#         'solve': 0.90
#         },
#         {'name': '普通物理-電、磁、光實驗',
#         'math': 0.90,
#         'coding': 0.00,
#         'logic': 0.90,
#         'creative': 0.30,
#         'solve': 1.20
#         },
#         {'name': '微積分(二)',
#         'math': 1.20,
#         'coding': 0.00,
#         'logic': 0.90,
#         'creative': 0.60,
#         'solve': 1.20
#         },
#         {'name': '微積分(二)實習',
#         'math': 1.20,
#         'coding': 0.00,
#         'logic': 0.90,
#         'creative': 0.60,
#         'solve': 1.20
#         },
#         {'name': '線性代數',
#         'math': 1.20,
#         'coding': 0.60,
#         'logic': 1.20,
#         'creative': 0.30,
#         'solve': 1.20
#         },
#         {'name': '邏輯設計',
#         'math': 0.60,
#         'coding': 0.60,
#         'logic': 1.20,
#         'creative': 0.60,
#         'solve': 0.90
#         },
#         {'name': '邏輯設計實習',
#         'math': 0.90,
#         'coding': 0.60,
#         'logic': 1.20,
#         'creative': 0.60,
#         'solve': 1.20
#         },
#         {'name': '通訊與網路概論',
#         'math': 1.20,
#         'coding': 0.60,
#         'logic': 1.20,
#         'creative': 0.60,
#         'solve': 1.20
#         },
#         {'name': '資料結構',
#         'math': 1.20,
#         'coding': 1.80,
#         'logic': 1.80,
#         'creative': 1.20,
#         'solve': 2.40
#         },
#         {'name': '資料結構實習',
#         'math': 1.20,
#         'coding': 2.40,
#         'logic': 1.80,
#         'creative': 1.20,
#         'solve': 2.40
#         },
#         {'name': '離散數學',
#         'math': 2.40,
#         'coding': 1.20,
#         'logic': 2.40,
#         'creative': 0.60,
#         'solve': 1.80
#         },
#         {'name': '系統程式',
#         'math': 0.60,
#         'coding': 1.80,
#         'logic': 1.80,
#         'creative': 1.20,
#         'solve': 2.40
#         },
#         {'name': '資料庫系統',
#         'math': 1.20,
#         'coding': 1.20,
#         'logic': 1.80,
#         'creative': 0.60,
#         'solve': 1.80
#         },
#         {'name': '幾率與統計',
#         'math': 1.80,
#         'coding': 0.00,
#         'logic': 1.20,
#         'creative': 0.60,
#         'solve': 1.20
#         },
#         {'name': '物件導向設計',
#         'math': 0.60,
#         'coding': 1.80,
#         'logic': 1.80,
#         'creative': 1.20,
#         'solve': 1.80
#         },
#         {'name': '物件導向設計實習',
#         'math': 0.00,
#         'coding': 1.80,
#         'logic': 1.80,
#         'creative': 1.80,
#         'solve': 2.40
#         },
#         {'name': '系統分析與設計',
#         'math': 0.60,
#         'coding': 1.20,
#         'logic': 1.80,
#         'creative': 1.20,
#         'solve': 1.80
#         },
#         {'name': '密碼學',
#         'math': 2.40,
#         'coding': 1.20,
#         'logic': 1.80,
#         'creative': 1.80,
#         'solve': 2.40
#         },
#         {'name': '電子商務安全',
#         'math': 0.60,
#         'coding': 1.20,
#         'logic': 1.20,
#         'creative': 0.60,
#         'solve': 1.80
#         },
#         {'name': '互聯網路',
#         'math': 1.20,
#         'coding': 1.20,
#         'logic': 1.80,
#         'creative': 1.20,
#         'solve': 1.80
#         },
#         {'name': '作業系統(一)',
#         'math': 1.80,
#         'coding': 2.70,
#         'logic': 3.60,
#         'creative': 1.80,
#         'solve': 3.60
#         },
#         {'name': '微處理機系統',
#         'math': 1.80,
#         'coding': 2.70,
#         'logic': 3.60,
#         'creative': 1.80,
#         'solve': 3.60
#         },
#         {'name': '微處理機系統實習',
#         'math': 1.80,
#         'coding': 2.70,
#         'logic': 3.60,
#         'creative': 1.80,
#         'solve': 3.60
#         },
#         {'name': '計算機演算法',
#         'math': 1.80,
#         'coding': 2.70,
#         'logic': 3.60,
#         'creative': 0.90,
#         'solve': 2.70
#         },
#         {'name': '計算機結構學',
#         'math': 0.90,
#         'coding': 1.80,
#         'logic': 2.70,
#         'creative': 1.80,
#         'solve': 2.70
#         },
#         {'name': '人工智慧導論',
#         'math': 2.70,
#         'coding': 2.70,
#         'logic': 2.70,
#         'creative': 1.80,
#         'solve': 2.70
#         },
#         {'name': '軟體工程開發實務',
#         'math': 0.90,
#         'coding': 3.60,
#         'logic': 2.70,
#         'creative': 2.70,
#         'solve': 3.60
#         },
#         {'name': '編譯器',
#         'math': 2.70,
#         'coding': 2.70,
#         'logic': 3.60,
#         'creative': 1.80,
#         'solve': 3.60
#         },
#         {'name': '程式語言',
#         'math': 0.90,
#         'coding': 2.70,
#         'logic': 2.70,
#         'creative': 1.80,
#         'solve': 2.70
#         },
#         {'name': '軟體測試',
#         'math': 0.90,
#         'coding': 0.90,
#         'logic': 2.70,
#         'creative': 1.80,
#         'solve': 2.70
#         },
#         {'name': '資料科學實務',
#         'math': 2.70,
#         'coding': 2.70,
#         'logic': 2.70,
#         'creative': 2.70,
#         'solve': 3.60
#         },
#         {'name': '資料探勘導論',
#         'math': 2.70,
#         'coding': 1.80,
#         'logic': 2.70,
#         'creative': 1.80,
#         'solve': 2.70
#         },
#         {'name': '資訊與網路安全',
#         'math': 2.70,
#         'coding': 2.70,
#         'logic': 3.60,
#         'creative': 2.70,
#         'solve': 3.60
#         },
#         {'name': '網路程式設計',
#         'math': 0.90,
#         'coding': 2.70,
#         'logic': 2.70,
#         'creative': 1.80,
#         'solve': 2.70
#         },
#         {'name': '網路程式設計實習',
#         'math': 0.00,
#         'coding': 3.60,
#         'logic': 2.70,
#         'creative': 0.90,
#         'solve': 3.60
#         },
#         {'name': '寬頻網路',
#         'math': 1.80,
#         'coding': 1.80,
#         'logic': 2.70,
#         'creative': 0.90,
#         'solve': 2.70
#         },
#         {'name': '資訊安全管理',
#         'math': 1.80,
#         'coding': 0.90,
#         'logic': 2.70,
#         'creative': 1.80,
#         'solve': 3.60
#         },
#         {'name': '安全程式設計',
#         'math': 2.70,
#         'coding': 2.70,
#         'logic': 3.60,
#         'creative': 1.80,
#         'solve': 3.60
#         },
#         {'name': '系統安全',
#         'math': 1.80,
#         'coding': 1.80,
#         'logic': 2.70,
#         'creative': 1.80,
#         'solve': 3.60
#         },
#         {'name': '無線網路系統',
#         'math': 2.40,
#         'coding': 1.20,
#         'logic': 2.40,
#         'creative': 1.20,
#         'solve': 2.40
#         },
#         {'name': '專題研究(一)',
#         'math': 2.40,
#         'coding': 3.60,
#         'logic': 3.60,
#         'creative': 2.40,
#         'solve': 3.60
#         },
#         {'name': '專題研究(二)',
#         'math': 2.40,
#         'coding': 4.80,
#         'logic': 4.80,
#         'creative': 3.60,
#         'solve': 4.80
#         }
#         # {'name': '計算機概論', 
#         #  'math':        1, 
#         #  'coding':      3, 
#         #  'logic':       3, 
#         #  'creative':    3, 
#         #  'solve':       3
#         #  },
#         #  {'name': '程式設計(I)', 
#         #  'math':        1, 
#         #  'coding':      3, 
#         #  'logic':       4, 
#         #  'creative':    2, 
#         #  'solve':       2
#         #  },
#         # Add more data as needed
#     ]

#     # Update the rows in the database using a loop.
#     for data in updated_data:
#         course_name = data['name']
#         course = CourseInfoModel.query.get(course_name)
        
#         if course:
#             course.math = data['math']
#             course.coding = data['coding']
#             course.logic = data['logic']
#             course.creative = data['creative']
#             course.solve = data['solve']
#             db.session.commit()

#     return "Updated successfully"


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

