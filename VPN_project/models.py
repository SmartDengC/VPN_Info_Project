import web
# import MySQLdb
# import pymysql


__db = web.database(
            dbn='mysql',
            user='root',
            pw='123456',
            db='dbname'
        )


def add(kwargs):
    # args = pymysql.escape_dict(args, charset='utf-8', mapping=None)
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
    __db.delete('todo', where={'USERID=$USERID'}, vars={'USERID': USERID})


def update(USERID, kwargs):
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


