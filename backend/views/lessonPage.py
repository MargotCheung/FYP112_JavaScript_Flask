from flask import render_template, url_for, request, jsonify, abort
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

def get_lesson_name():
    amount = request.args.get('amount', None)
    page = request.args.get('page', None)
    if amount is None and page is None:
        return abort(404)
    amount = int(amount)
    page = int(page)
    sql_query = 'SELECT course_name FROM course_info;'
    count = cursor.execute(sql_query)
    course_names = [row[0] for row in cursor.fetchall()]
    query_course_names = course_names[amount*page:amount*(page+1)]
    return jsonify(query_course_names=query_course_names)