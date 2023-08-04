from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from extends import db
from .form import RegisterForm, LoginForm
from models import UserModel
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            username = form.login_username.data
            password = form.login_password.data
            user = UserModel.query.filter_by(username=username).first()
            if not user:
                print("用戶不存在")
                return redirect(url_for("auth.login"))
            if (user.password == password):
                session['user_id'] = user.id
                return redirect("/")
            else:
                print("密碼錯誤")
                return redirect(url_for("auth.login"))
            return redirect(url_for("auth.register"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))

@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            return redirect(url_for("auth.register"))

@bp.route('/logout')
def logout():
    session.clear()
    return redirect("/")
