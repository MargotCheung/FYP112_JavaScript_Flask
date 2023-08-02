# session: 用來記錄cookie
# g: global（用來儲存已登入的用戶資料）
from flask import Flask, session, g

# config: config.py
import config

# 用來使用SQLAlchemy插件
from extends import db

# 資料庫的模型
from models import UserModel

# 每一個blueprints都要用不同名字來表示
from blueprints.course import bp as course_bp
from blueprints.auth import bp as auth_bp

# 美瞳models.py有更新都用migrate+upgrade一次
from flask_migrate import Migrate

app = Flask(__name__)

# 綁定配置文件
app.config.from_object(config)

# 初始化
db.init_app(app)

migrate = Migrate(app, db)

# 每一個blueprints都用這樣寫
app.register_blueprint(course_bp)
app.register_blueprint(auth_bp)

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

if __name__ == '__main__':
    app.run()
