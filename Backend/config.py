SECRET_KEY = "89kjb98ycgw98"

HOSTNAME    = '127.0.0.1'
PORT        = '3306'
DATABASE    = 'fengjia_db'
USERNAME    = 'root'
PASSWORD    = ''
DB_URI      = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI