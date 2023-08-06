from flask import render_template, url_for,request
from backend.db import cursor


def lessonPage_view():
    sql_query = 'SELECT course_name FROM course_info;'
    cursor.execute(sql_query)
    course_names = [row[0] for row in cursor.fetchall()]
   # 獲取當前顯示的course_name索引位置，預設為0
    current_index = int(request.args.get('index', 0))

    # 取出下一組五筆資料
    chunk_size = 5
    next_course_names = course_names[current_index:current_index+chunk_size]

    return render_template('lessonPage.html', **locals())

