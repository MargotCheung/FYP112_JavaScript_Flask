SECRET_KEY = "89kjb98ycgw98"

# 需要更改的就只有第6，7，8行的内容，分別是資料庫的名字，你的用戶名，你的密碼
HOSTNAME    = '127.0.0.1'
PORT        = '3306'
DATABASE    = 'fengjia_db'
USERNAME    = 'flask'
PASSWORD    = 'password'
DB_URI      = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI