from flask import render_template, url_for,request, g, redirect, flash
from backend.db import cursor, connection
from ..models import CommandModel, UserModel, LikeModel
from ..blueprints.form import CommandForm
from ..extends import db

def lessonDiscussion_view(course_name):
    user_id = g.user.id

    # 獲取 URL 中的 course_name 参数
    # course_name = request.args.get("course_name")  
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
            comments = CommandModel.query.filter_by(course_name=course_name).order_by(CommandModel.comment_time.desc()).all()
            user_id_to_username = {}
            for comment in comments:
                    user_id = comment.user_id
                    user = UserModel.query.get(user_id)
                    if user:
                        user_id_to_username[user_id] = user.username
        elif form.sort_by_oldest.data:
            comments = CommandModel.query.filter_by(course_name=course_name).order_by(CommandModel.comment_time.asc()).all()
            user_id_to_username = {}
            for comment in comments:
                    user_id = comment.user_id
                    user = UserModel.query.get(user_id)
                    if user:
                        user_id_to_username[user_id] = user.username
        else:
            comments = CommandModel.query.filter_by(course_name=course_name).all()
            user_id_to_username = {}
            for comment in comments:
                    user_id = comment.user_id
                    user = UserModel.query.get(user_id)
                    if user:
                        user_id_to_username[user_id] = user.username
        return render_template("lessonDiscussion.html",comments=comments, user_id_to_username=user_id_to_username, course_name=course_name)
    else:
        isCommanded = CommandModel.query.filter_by(course_name=course_name).first()
        
        if isCommanded:
            comments = CommandModel.query.filter_by(course_name=course_name).all()
            #讀ability
            user_id_to_username = {}
            for comment in comments:
                    user_id = comment.user_id
                    user = UserModel.query.get(user_id)
                    if user:
                        user_id_to_username[user_id] = user.username
            return render_template("lessonDiscussion.html",comments=comments, user_id_to_username=user_id_to_username, course_name=course_name)
        else:
            return render_template('lessonDiscussion.html', **locals())

def liked_view(course_name,comment_index):
    user_id = g.user.id
    comment = CommandModel.query.filter_by(index=comment_index)
    like = LikeModel.query.filter_by(author=user_id, comment_index=comment_index).first()
    # course_name = request.args.get("course_name") 

    if not comment:
        flash('Comment does exist.', category='error')
    elif like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = LikeModel(author=user_id, comment_index=comment_index)
        db.session.add(like)
        db.session.commit()
    
    return redirect(url_for('lessonDiscussion',course_name=course_name))
