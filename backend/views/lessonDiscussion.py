from flask import render_template, url_for,request, g, redirect, flash
from backend.db import cursor, connection
from ..models import CommandModel, UserModel, LikeModel
from ..blueprints.form import CommandForm
from ..extends import db

def lessonDiscussion_view():
    user_id = g.user.id
    #讀ability
    sql_query = f"SELECT * FROM user_profile WHERE id = {user_id};"
    cursor.execute(sql_query)
    credit = cursor.fetchall()

    # 獲取 URL 中的 course_name 参数
    course_name = request.args.get("course_name")  
    # 留言板
    if request.method == "POST":
        form = CommandForm(request.form)
        print(form.sort_by_latest.data)
        if form.validate():
            content = form.commandcontent.data
            comment = CommandModel(course_name=course_name, user_id=user_id, response=content)
            db.session.add(comment)
            db.session.commit()
        if form.sort_by_latest.data:
            posts = CommandModel.query.filter_by(course_name=course_name).order_by(CommandModel.command_time.desc()).all()
            user_id_to_username = {}
            for post in posts:
                    user_id = post.user_id
                    user = UserModel.query.get(user_id)
                    if user:
                        user_id_to_username[user_id] = user.username
        elif form.sort_by_oldest.data:
            posts = CommandModel.query.filter_by(course_name=course_name).order_by(CommandModel.command_time.asc()).all()
            user_id_to_username = {}
            for post in posts:
                    user_id = post.user_id
                    user = UserModel.query.get(user_id)
                    if user:
                        user_id_to_username[user_id] = user.username
        else:
            posts = CommandModel.query.filter_by(course_name=course_name).all()
            user_id_to_username = {}
            for post in posts:
                    user_id = post.user_id
                    user = UserModel.query.get(user_id)
                    if user:
                        user_id_to_username[user_id] = user.username
        return render_template("lessonDiscussion.html",posts=posts, user_id_to_username=user_id_to_username, course_name=course_name)
    else:
        isCommanded = CommandModel.query.filter_by(course_name=course_name).first()
        
        if isCommanded:
            posts = CommandModel.query.filter_by(course_name=course_name).all()
            #讀ability
            user_id_to_username = {}
            for post in posts:
                    user_id = post.user_id
                    user = UserModel.query.get(user_id)
                    if user:
                        user_id_to_username[user_id] = user.username
            return render_template("lessonDiscussion.html",posts=posts, user_id_to_username=user_id_to_username, course_name=course_name)
        else:
            return render_template('lessonDiscussion.html', **locals())

def liked_view(comment_index):
    comment = CommandModel.query.filter_by(index=comment_index)
    like = LikeModel.query.filter_by(index=comment_index)

    if not comment:
         flash('Comment does exist.', category='error')