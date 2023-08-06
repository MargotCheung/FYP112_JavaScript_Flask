from flask import render_template, url_for
from backend.db import cursor


def lessonPage_view():
    # sql_query = 'SELECT * FROM course_info;'
    # cursor.execute(sql_query)
    # course_info = cursor.fetchall()
    # cursor.close()
    return render_template('lessonPage.html', **locals())

