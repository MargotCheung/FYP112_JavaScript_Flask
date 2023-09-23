from flask import render_template, url_for, request, jsonify, abort,g
from backend.db import cursor
from ..models import UserGradeModel, CourseInfoModel, UserModel
from ..extends import db
from ..blueprints.form import MyResultSearchForm

def lessonPage_view():
    user_id = g.user.id
    #讀ability
    sql_query = f"SELECT * FROM user_profile WHERE id = {user_id};"
    cursor.execute(sql_query)
    credit = cursor.fetchall()

    sql_query = 'SELECT course_name FROM course_info;'
    cursor.execute(sql_query)
    course_names = [row[0] for row in cursor.fetchall()]
   # 獲取當前顯示的course_name索引位置，預設為0
    current_index = int(request.args.get('index', 0))

    # 取出下一組五筆資料
    chunk_size = 5
    next_course_names = course_names[current_index:current_index+chunk_size]

    return render_template('lessonPage.html', **locals())

# [
#     {
#         'name': 'asdkjfaksj',
#         'id': 293,
#         'introduction': 'akdfj'
#     },
#     {
#         'name': 'qpweiruqwpi',
#         'id': 87,
#         'introduction': 'aqiwuerio'
#     }
# ]

def get_lesson_name():
    user_id = g.user.id
    # 得到user的全部内容，後續都會用到
    user = UserModel.query.filter_by(id=user_id).first()

    amount = request.args.get('amount', None)
    page = request.args.get('page', None)
    if amount is None and page is None:
        return abort(404)
    amount = int(amount)
    page = int(page)
    sql_query = 'SELECT * FROM course_info;'
    count = cursor.execute(sql_query)
    course_names = []
    for row in cursor.fetchall():
        course = {
            'course_name': row[0],
            'course_year': row[1],
            'course_type': row[2],
            'course_credit': row[3],
            'course_intro': row[4],
            'math': row[5],
            'coding': row[6],
            'logic': row[7],
            'creative': row[8],
            'slove': row[9],
        }
        temp=0
        if user.ability_math >= row[5]:
            temp+=1
        if user.ability_coding >= row[6]:
            temp+=1
        if user.ability_logic >= row[7]:
            temp+=1
        if user.ability_creative >= row[8]:
            temp+=1
        if user.ability_solve >= row[9]:
            temp+=1
        # # 计算 ability，这里假设将 math、coding、logic、creative、slove 相加
        # ability = row[5] + row[6] + row[7] + row[8] + row[9]
        if temp>3:
            ability="綽綽有餘"
        elif temp==3:
            ability="還可以"
        elif temp==2:
            ability="有點勉強"
        elif temp<2:
            ability="不太推薦"
        course['ability'] = ability  # 将计算结果添加到字典中
        course_names.append(course)  # 将字典添加到列表中

    query_course_names = course_names[amount*page:amount*(page+1)]
    return jsonify(query_course_names=query_course_names)