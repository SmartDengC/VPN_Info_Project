import web
import DBUtils

db = web.database(
    maxconnections=10,
    dbn='mysql',
    user='root',
    pw='123456',
    db='dbname'
)
