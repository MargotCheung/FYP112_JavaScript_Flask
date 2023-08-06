from flask import render_template, url_for
from backend.db import cursor

# 舊的手刻板
def lessonpage_view(row_course_name):
    sql_query = f"SELECT * FROM lesson_response WHERE course_name = '{row_course_name}';"
    cursor.execute(sql_query)
    lesson_response = cursor.fetchall()

    sql_query = "SELECT course_name, tc_name FROM course_teacher;"
    cursor.execute(sql_query)
    course_teacher_data = cursor.fetchall()

    return render_template('lessonpage.html', **locals())