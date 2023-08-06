from flask import render_template, url_for
from backend.db import cursor


def learningProgress_view(user_id):
    sql_query = f"SELECT * FROM user_profile WHERE user_id = '{user_id}';"
    cursor.execute(sql_query)
    credit = cursor.fetchall()
    # print(credit[5])
    return render_template('learningProgress.html', **locals())


# if __name__ == "__main__":
#     app.run(debug=True)