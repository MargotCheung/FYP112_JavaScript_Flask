from flask import render_template, url_for, request, jsonify, g, redirect, flash
from backend.db import cursor, connection
from ..models import UserGradeModel, CourseInfoModel, UserModel
from ..extends import db
from ..blueprints.form import MyResultSearchForm

def learningProgress_view():
    form = MyResultSearchForm()
    form.course_name.choices = [(0,'科目名稱')]
    user_id = g.user.id
    
    # 得到user的全部内容，後續都會用到
    user = UserModel.query.filter_by(id=user_id).first()
    
    # 蜘蛛網圖的資料
    chart_data = [user.ability_math, user.ability_coding, user.ability_creative, user.ability_solve, user.ability_logic]

    # 利用course_name找出對應的coursetype和coursecredit，存在dictionary裏
    grades = UserGradeModel.query.filter_by(user_id=user_id).all()
    coursetype = {}
    for course in grades:
        course_name = course.course_name
        course_info = CourseInfoModel.query.get(course_name)
        if course_info:
            coursetype[course.index] = course_info.course_type

    coursecredit = {}
    for course in grades:
        course_name = course.course_name
        course_info = CourseInfoModel.query.get(course_name)
        if course_info:
            coursecredit[course.index] = course_info.course_credit

    # 當按下“上傳”
    if request.method == "POST":
        # 上傳成績
        postform = MyResultSearchForm(request.form)
        grade = postform.course_year.data
        course_name = postform.course_name.data
        score = postform.score.data
        

        course = CourseInfoModel.query.filter_by(course_name=course_name).first()
        # 檢查有沒有該course，主要是防呆
        if course:
            #找出course_info 中的course_type
            sql_query = f"SELECT course_type FROM course_info WHERE course_name = '{course_name}';"
            cursor.execute(sql_query)
            course_type_data= cursor.fetchone()
            #找出course_info 中的course_credit
            # sql_query = f"SELECT course_credit FROM course_info WHERE course_name = '{course_name}';"
            # cursor.execute(sql_query)
            # course_credit_data= cursor.fetchone()
            # print("看這裡"+course_credit_data[0])

            star_math = 0
            star_coding = 0
            star_logic = 0
            star_creative = 0
            star_solve = 0

            if course_type_data[0]=='必修':
                # 計算每個年級的必修各自能力值星號的加權
                sql_query = f"SELECT * FROM course_info WHERE course_year = '{grade}' AND course_type = '必修';"
                cursor.execute(sql_query)
                ability_data_major = cursor.fetchall()

                for item in ability_data_major:
                    star_math += item[5]
                    star_coding += item[6]
                    star_logic += item[7]
                    star_creative += item[8]
                    star_solve += item[9]

                star_math = round(1 / star_math, 2)
                star_coding = round(1 / star_coding, 2)
                star_logic = round(1 / star_logic, 2)
                star_creative = round(1 / star_creative, 2)
                star_solve = round(1 / star_solve, 2)
                


            # 確認想要上傳的成績是不是已經存在，如果是已經存在會變成更新分數
            isUpdate = UserGradeModel.query.filter_by(user_id=user_id,course_name=course_name).first()
            if isUpdate:
                # 先減去原本已加入的能力值
                beforeUpdate = isUpdate.score
                beforeMath = isUpdate.course_math
                beforeCoding = isUpdate.course_coding
                beforeLogic = isUpdate.course_logic
                beforeCreative = isUpdate.course_creative
                beforeSolve = isUpdate.course_solve
                # print(beforeMath)

                user.ability_math -= beforeMath
                user.ability_coding -= beforeCoding
                user.ability_logic -= beforeLogic
                user.ability_creative -= beforeCreative
                user.ability_solve -= beforeSolve
                
                db.session.commit()
                
                # 計算更新後的成績能力值后，加入user的能力值 
                isUpdate.score = score
                if course_type_data[0]=='必修':
                    course_math = (course.math *star_math* score) / 100
                    course_coding = (course.coding *star_coding* score) / 100
                    course_logic = (course.logic *star_logic* score) / 100
                    course_creative = (course.creative *star_creative* score) / 100
                    course_solve = (course.solve *star_solve* score) / 100
                elif course_type_data[0]=='選修':
                    course_math = (course.math *0.02* score) / 100
                    course_coding = (course.coding *0.02* score) / 100
                    course_logic = (course.logic *0.02* score) / 100
                    course_creative = (course.creative *0.02* score) / 100
                    course_solve = (course.solve *0.02* score) / 100
                    
                Update_course_math = course_math
                Update_course_coding = course_coding
                Update_course_logic = course_logic
                Update_course_creative = course_creative
                Update_course_solve = course_solve

                user.ability_math += Update_course_math
                user.ability_coding += Update_course_coding
                user.ability_logic += Update_course_logic
                user.ability_creative += Update_course_creative
                user.ability_solve += Update_course_solve
                db.session.commit()
            else:
                # 計算成績能力值加入user的能力值
                # 計算必修的能力值
                if course_type_data[0]=='必修':
                    course_math = (course.math *star_math* score) / 100
                    course_coding = (course.coding *star_coding* score) / 100
                    course_logic = (course.logic *star_logic* score) / 100
                    course_creative = (course.creative *star_creative* score) / 100
                    course_solve = (course.solve *star_solve* score) / 100
                elif course_type_data[0]=='選修':
                    course_math = (course.math *0.02* score) / 100
                    course_coding = (course.coding *0.02* score) / 100
                    course_logic = (course.logic *0.02* score) / 100
                    course_creative = (course.creative *0.02* score) / 100
                    course_solve = (course.solve *0.02* score) / 100
                    
                user.ability_math += course_math
                user.ability_coding += course_coding
                user.ability_logic += course_logic
                user.ability_creative += course_creative
                user.ability_solve += course_solve

                # 新增成績
                addgrade = UserGradeModel(user_id=user_id, grade=grade, course_name=course_name, score=score,course_math=course_math,course_coding=course_coding,course_logic=course_logic,course_creative=course_creative,course_solve=course_solve)
                db.session.add(addgrade)
                db.session.commit()

                # # 更新用户的学分数据&&能力值
                # user_profile_query = f"SELECT * FROM user_profile WHERE username = '{user_id}';"
                # cursor.execute(user_profile_query)
                # user_profile_data = cursor.fetchone()
                # # print(user_profile_data)
                # if user_profile_data: 
                #     print("有近來")
                #     if course_type_data[0]=='必修':
                #         updated_credit = user_profile_data[9] + int(course_credit_data[0])
                #         # 使用 UPDATE 查询更新数据库中的数据
                #         update_query = f"UPDATE user_profile SET complete_credit_major = {updated_credit} WHERE username = '{user_id}';"
                #     elif course_type_data[0]=='選修': 
                #         updated_credit = user_profile_data[11] + int(course_credit_data[0])
                #         update_query = f"UPDATE user_profile SET complete_credit_elec = {updated_credit} WHERE username = '{user_id}';"    
                #     elif course_type_data[0]=='通識':    
                #         updated_credit = user_profile_data[13] + int(course_credit_data[0])
                #         update_query = f"UPDATE user_profile SET complete_credit_general = {updated_credit} WHERE username = '{user_id}';"
                #     elif course_type_data[0]=='系外選修':    
                #         updated_credit = user_profile_data[15] + int(course_credit_data[0])
                #         update_query = f"UPDATE user_profile SET complete_credit_outer = {updated_credit} WHERE username = '{user_id}';"    
                #     cursor.execute(update_query)
                #     connection.commit()

            return redirect(url_for('learningProgress'))
        else:
            flash('請選擇列表')

    return render_template('learningProgress.html', posts=form, allgrades=grades, course_type=coursetype, course_credit=coursecredit, **locals())

# 動態下拉式選單
def profileDroplist_view(course_year):
    courseArray=[]
    
    # course_year=0是因爲0="年級"
    if course_year == '0':
        courseObj = {}
        courseObj['course_name'] = '科目名稱'
        courseArray.append(courseObj)
    else:
        # 把年級傳進來后，找出對應的course_name，再用json檔傳出去
        courses = CourseInfoModel.query.filter_by(course_year=course_year).all()
        for course in courses:
            courseObj = {}
            courseObj['course_name'] = course.course_name
            courseArray.append(courseObj)

    return jsonify({'courses' : courseArray})

# def save_data(course_name):
#     # 接收通过AJAX发送的数据
#     data = request.form  # 接收前端发送的JSON数据
#     # print(data)
#     # save_data(data)  # 调用save_data()函数来保存数据
#     user_id= g.user.id
#     grade = data.get('grade')
#     course_name = data.get('course_name')
#     # course_type = data.get('course_type')
#     # course_credit = data.get('course_credit')
#     score = data.get('score')
#     # 存進user_grade
#     # sql_query = f'INSERT INTO user_grades (user_id, grade, course_name, course_type, course_credit, score) VALUES ("{user_id}","{grade}", "{course_name}","{course_type}","{course_credit}","{score}")'
#     insert = UserGradeModel(user_id=user_id,grade=grade,course_name=course_name)
#     # like = LikeModel(author=user_id, comment_index=comment_index)
#     db.session.add(insert)
#     db.session.commit()

#     # 計算user能力值
#     user_ability = f"SELECT * FROM course_info WHERE course_name = '{course_name}';"
#     cursor.execute(user_ability)
#     user_ability_data = cursor.fetchone()
#     # 將course的能力值存起來並做計算
#     if user_ability_data is not None:
#         ability_math = user_ability_data[6] * 0.1
#         ability_coding = user_ability_data[7] * 0.1
#         ability_logic = user_ability_data[8] * 0.1
#         ability_creative = user_ability_data[9] * 0.1
#         ability_solve = user_ability_data[10] * 0.1
#         # ... 继续处理能力值和更新操作 ...
#     else:
#         print("No data found for course:", course_name)

#     # 更新用户的学分数据&&能力值
#     user_profile_query = f"SELECT * FROM user_profile WHERE user_id = '{user_id}';"
#     cursor.execute(user_profile_query)
#     user_profile_data = cursor.fetchone()
#     # print(user_profile_data)
#     if user_profile_data:
#         ability_math    = user_profile_data[15]+ability_math
#         ability_coding  = user_profile_data[16]+ability_coding
#         ability_logic   = user_profile_data[17]+ability_logic
#         ability_creative= user_profile_data[18]+ability_creative
#         ability_solve   = user_profile_data[19]+ability_solve  
#         if course_type == "系院必修":
#             updated_credit = user_profile_data[8] + int(course_credit)
#             # 使用 UPDATE 查询更新数据库中的数据
#             update_query = f"UPDATE user_profile SET complete_credit_major = {updated_credit},ability_math = {ability_math},ability_coding = {ability_coding},ability_logic = {ability_logic},ability_creative = {ability_creative},ability_solve = {ability_solve} WHERE user_id = '{user_id}';"
#         elif course_type == "系院選修":    
#             updated_credit = user_profile_data[10] + int(course_credit)
#             update_query = f"UPDATE user_profile SET complete_credit_elec = {updated_credit},ability_math = {ability_math},ability_coding = {ability_coding},ability_logic = {ability_logic},ability_creative = {ability_creative},ability_solve = {ability_solve} WHERE user_id = '{user_id}';"    
#         elif course_type == "通識":    
#             updated_credit = user_profile_data[12] + int(course_credit)
#             update_query = f"UPDATE user_profile SET complete_credit_general = {updated_credit},ability_math = {ability_math},ability_coding = {ability_coding},ability_logic = {ability_logic},ability_creative = {ability_creative},ability_solve = {ability_solve} WHERE user_id = '{user_id}';"
#         elif course_type == "系外選修":    
#             updated_credit = user_profile_data[14] + int(course_credit)
#             update_query = f"UPDATE user_profile SET complete_credit_outer = {updated_credit},ability_math = {ability_math},ability_coding = {ability_coding},ability_logic = {ability_logic},ability_creative = {ability_creative},ability_solve = {ability_solve} WHERE user_id = '{user_id}';"    
#         cursor.execute(update_query)
#         connection.commit()

    

#     return jsonify({'message': 'Grade submitted successfully'})

# if __name__ == "__main__":
#     app.run(debug=True)