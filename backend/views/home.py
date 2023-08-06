import sqlite3
from flask import render_template, url_for
from backend.db import cursor


def home_view():
    # sql_query = 'SELECT * FROM course_info;'
    # cursor.execute(sql_query)
    # course_info = cursor.fetchall()
    # cursor.close()
    return render_template('homepage.html', **locals())



    # sql_query = 'SELECT course_name FROM course_info;'
    # cursor.execute(sql_query)
    # course_name = cursor.fetchall()
    # cursor.close()
    # return render_template('homepage.html', **locals())