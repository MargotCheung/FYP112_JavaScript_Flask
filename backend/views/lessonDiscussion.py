from flask import render_template, url_for,request, g
from backend.db import cursor, connection

def lessonDiscussion_view():
    user_id = g.user.username
    #讀ability
    sql_query = f"SELECT * FROM user_profile WHERE user_id = '{user_id}';"
    cursor.execute(sql_query)
    credit = cursor.fetchall()

    # 獲取 URL 中的 course_name 参数
    course_name = request.args.get("course_name")  
    print("Course Name:", course_name)
    # 留言板
    # 獲取從ajax傳過來的參數
    if request.method == "POST":
        course_name = request.form.get("course_name") 
        message = request.form.get("message")
        user_id= g.user.username
        if message and course_name:
            sql_query = f'INSERT INTO lesson_response (course_name, user_id, response) VALUES ("{course_name}", "{user_id}", "{message}")'
            # values = (course_name, user_id, message)
            cursor.execute(sql_query)
            connection.commit()  # 提交更改到資料庫
            # return "留言已提交"



    if course_name:
        sql_query = f"SELECT * FROM lesson_response WHERE course_name = '{course_name}'"
        cursor.execute(sql_query)
        course_data = cursor.fetchall()

        user_id = g.user.username
        #讀ability
        sql_query = f"SELECT * FROM user_profile WHERE user_id = '{user_id}';"
        cursor.execute(sql_query)
        credit = cursor.fetchall()
        # print(course_data)
        return render_template("lessonDiscussion.html", course_data=course_data,credit=credit)
    else:
        return "Course name parameter is missing."


    return render_template('lessonDiscussion.html', **locals())

    # sql_query = f"SELECT * FROM course_response WHERE course_name = '{course_name}';"
    # cursor.execute(sql_query)
    # course_info = cursor.fetchall()
    # cursor.close()