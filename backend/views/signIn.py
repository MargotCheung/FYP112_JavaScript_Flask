from flask import render_template, url_for
from backend.db import cursor

# 舊的手刻板
def signIn_view():
    # sql_query = f"SELECT * FROM lesson_response WHERE course_name = '{row_course_name}';"
    # cursor.execute(sql_query)
    # lesson_response = cursor.fetchall()
    return render_template('signIn.html', **locals())