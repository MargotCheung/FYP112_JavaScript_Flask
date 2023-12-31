import wtforms
from wtforms.validators import Email, Length, EqualTo
from models import UserModel

# 驗證數據是否符合要求
class RegisterForm(wtforms.Form):
    username = wtforms.StringField('username', validators=[Length(min=3, max=20, message="用戶名長度必須在3到20字内!")])
    email = wtforms.EmailField('email', validators=[Email(message="郵箱格式錯誤!")])
    password = wtforms.PasswordField('password', validators=[Length(min=6, max=20, message="密碼長度必須在6到20字内!")])
    confirm_password = wtforms.PasswordField('confirm_password', validators=[EqualTo("password", message="密碼必須一樣!")])

    # 驗證郵箱是否重複
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="該郵箱已被注冊！")

class LoginForm(wtforms.Form):
    login_username = wtforms.StringField('login_username', validators=[Length(min=3, max=20, message="用戶名長度必須在3到20字内!")])
    login_password = wtforms.PasswordField('login_password', validators=[Length(min=6, max=20, message="密碼長度必須在6到20字内!")])