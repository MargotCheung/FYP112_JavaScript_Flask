from flask import render_template, url_for, request, jsonify, g
from backend.db import cursor, connection


def learningProgress_view():
    user_id = g.user.username
    print(user_id)
    sql_query = f"SELECT * FROM user_profile WHERE user_id = '{user_id}';"
    cursor.execute(sql_query)
    credit = cursor.fetchall()
    # print(credit[5])
    sql_query = f"SELECT * FROM user_grades WHERE user_id = '{user_id}';"
    cursor.execute(sql_query)
    grades = cursor.fetchall()
    # print(grades[1])
    return render_template('learningProgress.html', **locals())

def save_data():
    # 接收通过AJAX发送的数据
    data = request.form  # 接收前端发送的JSON数据
    # print(data)
    # save_data(data)  # 调用save_data()函数来保存数据
    user_id= g.user.username 
    grade = data.get('grade')
    course_name = data.get('course_name')
    course_type = data.get('course_type')
    course_credit = data.get('course_credit')
    score = data.get('score')
    # 存進user_grade
    sql_query = f'INSERT INTO user_grades (user_id, grade, course_name, course_type, course_credit, score) VALUES ("{user_id}","{grade}", "{course_name}","{course_type}","{course_credit}","{score}")'
    cursor.execute(sql_query)
    connection.commit()

    user_profile_query = f"SELECT * FROM user_profile WHERE user_id = '{user_id}';"
    cursor.execute(user_profile_query)
    user_profile_data = cursor.fetchone()
    # print(user_profile_data)
    if user_profile_data:
        if course_type == "系院必修":
           # 更新用户的学分数据
            updated_credit = user_profile_data[8] + int(course_credit)
            # 使用 UPDATE 查询更新数据库中的数据
            update_query = f"UPDATE user_profile SET complete_credit_major = {updated_credit} WHERE user_id = '{user_id}';"
        elif course_type == "系院選修":    
            updated_credit = user_profile_data[10] + int(course_credit)
            update_query = f"UPDATE user_profile SET complete_credit_elec = {updated_credit} WHERE user_id = '{user_id}';"    
        elif course_type == "通識":    
            updated_credit = user_profile_data[12] + int(course_credit)
            update_query = f"UPDATE user_profile SET complete_credit_general = {updated_credit} WHERE user_id = '{user_id}';"
        elif course_type == "系外選修":    
            updated_credit = user_profile_data[14] + int(course_credit)
            update_query = f"UPDATE user_profile SET complete_credit_outer = {updated_credit} WHERE user_id = '{user_id}';"
              
        cursor.execute(update_query)
        connection.commit()
    return jsonify({'message': 'Grade submitted successfully'})

# if __name__ == "__main__":
#     app.run(debug=True)