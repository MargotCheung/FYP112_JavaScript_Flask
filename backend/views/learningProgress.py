from flask import render_template, url_for, request, jsonify
from backend.db import cursor


def learningProgress_view(user_id):
    sql_query = f"SELECT * FROM user_profile WHERE user_id = '{user_id}';"
    cursor.execute(sql_query)
    credit = cursor.fetchall()
    # print(credit[5])
    return render_template('learningProgress.html', **locals())

def save_data(data):
    # 接收通过AJAX发送的数据
    # data = request.json 
    # print(data)
    # user_id = data.get('user_id')
    user_id="007"  
    grade = data.get('grade')
    course_name = data.get('course_name')
    course_type = data.get('course_type')
    course_credit = data.get('course_credit')
    score = data.get('score')

    sql_query = f'INSERT INTO user_grades (user_id, grade, subject, category, credits, score) VALUES ("{user_id}","{grade}", "{course_name}","{course_type}","{course_credit}","{score}")'
    # values = (grade, subject, category, credits, score)
    cursor.execute(sql_query)
    connection.commit()

    # 返回响应
    return jsonify({'message': 'Grade submitted successfully'})

# if __name__ == "__main__":
#     app.run(debug=True)