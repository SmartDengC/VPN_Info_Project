import web
import json
# import MySQLdb
# import pymysql


__db = web.database(
            dbn='mysql',
            user='root',
            pw='123456',
            db='dbname'
        )


def add(kwargs):
    __db.insert(
        'todo',
        USERNAME=kwargs['USERNAME'],
        IDCARD=kwargs['IDCARD'],
        TEL=kwargs['TEL'],
        APPLICANT=kwargs['APPLICANT'],
        DEPARTMENT=kwargs['DEPARTMENT'],
        VPNACCOUT=kwargs['VPNACCOUT'],
        PASSWORD=kwargs['PASSWORD'],
        STARTIME=kwargs['STARTIME'],
        ENDTIME=kwargs['ENDTIME'],
        ACCTYPE=kwargs['ACCTYPE'],
        SERVERIP=kwargs['SERVERIP'],
        SERVERPORT=kwargs['SERVERPORT']
    )


# 控制层传以userid
def delete(USERID):
    __db.query('DELETE FROM todo WHERE USERID=%s' % USERID)


def modify(USERID, kwargs):
    __db.update(
        'todo',
        where={'USERID=$USERID'},
        vars={'USERID': USERID},
        USERNAME=kwargs['USERNAME'],
        IDCARD=kwargs['IDCARD'],
        TEL=kwargs['TEL'],
        APPLICANT=kwargs['APPLICANT'],
        DEPARTMENT=kwargs['DEPARTMENT'],
        VPNACCOUT=kwargs['VPNACCOUT'],
        PASSWORD=kwargs['PASSWORD'],
        STARTIME=kwargs['STARTIME'],
        ENDTIME=kwargs['ENDTIME'],
        ACCTYPE=kwargs['ACCTYPE'],
        SERVERIP=kwargs['SERVERIP'],
        SERVERPORT=kwargs['SERVERPORT']
    )


def select(USERID):
    result = __db.select(
        'todo',
        where='USERID=$USERID',
        vars={'USERID': USERID}
    )
    return result


def select_all():
    result = __db.select('todo')
    return result


if __name__ == '__main__':
    length = {
        'USERNAME': 'jet',
        'IDCARD': '',
        'TEL': '18328377763',
        'APPLICANT': 'jet',
        'DEPARTMENT': 'jet',
        'VPNACCOUT': 'jet',
        'PASSWORD': 'jet',
        'STARTIME': '2018-2-2',
        'ENDTIME': '2018-5-6',
        'ACCTYPE': 'jet',
        'SERVERIP': 'jet',
        'SERVERPORT': 'jet'
    }
    print(type(length))
    # update(1, length)
    user = "{'name' : 'jim', 'sex' : 'male', 'age': 18}"
    print(user, 'type', type(user))
    b = eval(user)
    print(b, 'type', type(b))
    c = exec(user)
    print(c, 'type', type(c))