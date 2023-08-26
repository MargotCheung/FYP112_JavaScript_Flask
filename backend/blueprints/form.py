import wtforms
from wtforms.validators import Email, Length, EqualTo
from ..models import UserModel

# 驗證數據是否符合要求
class RegisterForm(wtforms.Form):
    RegisterDefaultUsername = wtforms.StringField('RegisterDefaultUsername', validators=[Length(min=3, max=20, message="用戶名長度必須在3到20字内!")])
    RegisterDefaultEmail = wtforms.EmailField('RegisterDefaultEmail', validators=[Email(message="郵箱格式錯誤!")])
    RegisterDefaultPassword1 = wtforms.PasswordField('RegisterDefaultPassword1', validators=[Length(min=6, max=20, message="密碼長度必須在6到20字内!")])
    RegisterDefaultPassword2 = wtforms.PasswordField('RegisterDefaultPassword2', validators=[EqualTo("RegisterDefaultPassword1", message="密碼必須一樣!")])

    # 驗證郵箱是否重複
    def validate_email(self, field):
        RegisterDefaultEmail = field.data
        user = UserModel.query.filter_by(email=RegisterDefaultEmail).first()
        if user:
            raise wtforms.ValidationError(message="該郵箱已被注冊！")

class LoginForm(wtforms.Form):
    validationDefaultEmail = wtforms.StringField('validationDefaultEmail', validators=[Length(min=3, max=20, message="用戶名長度必須在3到20字内!")])
    validationDefaultUsername = wtforms.PasswordField('validationDefaultUsername', validators=[Length(min=6, max=20, message="密碼長度必須在6到20字内!")])