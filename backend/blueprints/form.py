import wtforms
from wtforms.validators import Email, Length, EqualTo, NumberRange, DataRequired
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

class CommandForm(wtforms.Form):
    commandcontent = wtforms.TextAreaField('commandcontent', validators=[Length(min=1)])
    sort_by_latest = wtforms.SubmitField('由新到舊')
    sort_by_oldest = wtforms.SubmitField('由舊到新')

class MyResultSearchForm(wtforms.Form):
    course_year = wtforms.SelectField('年級', choices=[(0,'年級'),(1,'大一'),(2,'大二'),(3,'大三'),(4,'大四')])
    course_name = wtforms.SelectField('科目名稱', choices=[])
    score = wtforms.IntegerField('分數', validators=[NumberRange(min=0, max=100, message="less then 0 or more then 100")])

class UploadPaperForm(wtforms.Form):
    year = wtforms.IntegerField('年份')
    course = wtforms.StringField('科目')
    teacher = wtforms.StringField('老師')
    pdf_file = wtforms.FileField('Upload PDF File')
    info = wtforms.TextAreaField('詳情', validators=[Length(min=1)])
    submit = wtforms.SubmitField('Submit')