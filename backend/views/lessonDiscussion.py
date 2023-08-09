from flask import render_template, url_for,request
from backend.db import cursor
import sqlite3

def lessonDiscussion_view():
    # 获取 URL 中的 course_name 参数
    course_name = request.args.get("course_name")  

    if course_name:
        # 使用 course_name 进行数据库查询
        sql_query = f"SELECT * FROM lesson_response WHERE course_name = '{course_name}'"
        cursor.execute(sql_query)
        course_data = cursor.fetchall()
        # print(course_data)

        return render_template("lessonDiscussion.html", course_data=course_data)
    
    return "Course name parameter is missing."
    # sql_query = f"SELECT * FROM course_response WHERE course_name = '{course_name}';"
    # cursor.execute(sql_query)
    # course_info = cursor.fetchall()
    # cursor.close()
    return render_template('lessonDiscussion.html', **locals())

