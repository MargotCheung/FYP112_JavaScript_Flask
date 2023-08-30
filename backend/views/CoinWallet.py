from flask import render_template, url_for,g
from backend.db import cursor


def CoinWallet_view():
    user_id = g.user.username
    #讀ability
    sql_query = f"SELECT * FROM user_profile WHERE user_id = '{user_id}';"
    cursor.execute(sql_query)
    credit = cursor.fetchall()
    return render_template('CoinWallet.html', **locals())

