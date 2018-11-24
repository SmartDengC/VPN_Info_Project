# -*- coding: utf-8 -*-
import web
from db import db

urls = (
    '/user/(\d+)', 'user',
    '/users', 'users'
)


class user:
    # 获取某个用户的信息

    def GET(self, USERID):
        USERID = int(USERID)
        datas = []
        if db:
            result = db.select(
                'todo',
                where='USERID=$USERID',
                vars={'USERID': USERID}
            )
            for i, j in enumerate(result):
                out_j = dict(j)
                datas.append(out_j)
            return datas
        else:
            return 'error'

class users:
    # 获取所有的人员信息
    def GET(self):
        result = db.select('todo')
        list_from_db = []
        for menber in result:
            temp = dict()
            for key in menber:
                temp[key] = menber[key]
            list_from_db.append(temp)
        return list_from_db
    # 对用户进行操作 增改删
    def POST(self):
        '''
        1:使用web.data()从请求体中获取参数，实现用户添加

        2:主要思路：首先只有一个POST方法（可以有多个）,根据 USERID 这个特殊的字段

        如果 只有USERID 则根据USERID 删除
        如果有USERID 也有 USERNAME 则修改
        如果有没有USERID 则增加
        '''

        info = web.data()
        info = str(info, encoding='utf-8')
        info = eval(info)
        if ('USERID' not in info.keys()):
            db.insert(
                'todo',
                USERNAME=info['USERNAME'],
                IDCARD=info['IDCARD'],
                TEL=info['TEL'],
                APPLICANT=info['APPLICANT'],
                DEPARTMENT=info['DEPARTMENT'],
                VPNACCOUT=info['VPNACCOUT'],
                PASSWORD=info['PASSWORD'],
                STARTIME=info['STARTIME'],
                ENDTIME=info['ENDTIME'],
                ACCTYPE=info['ACCTYPE'],
                SERVERIP=info['SERVERIP'],
                SERVERPORT=info['SERVERPORT'])
            return 'addition is ok!'
        else:
            if ('USERNAME' not in info.keys()):
                db.delete(
                    'todo',
                    where='USERID=$USERID',
                    vars={
                        'USERID': info['USERID']
                    })
                return 'deletion is ok'
            else:
                db.update(
                    'todo',
                    where='USERID=$USERID',
                    vars={
                        'USERID': info['USERID']
                    },
                    USERNAME=info['USERNAME'],
                    IDCARD=info['IDCARD'],
                    TEL=info['TEL'],
                    APPLICANT=info['APPLICANT'],
                    DEPARTMENT=info['DEPARTMENT'],
                    VPNACCOUT=info['VPNACCOUT'],
                    PASSWORD=info['PASSWORD'],
                    STARTIME=info['STARTIME'],
                    ENDTIME=info['ENDTIME'],
                    ACCTYPE=info['ACCTYPE'],
                    SERVERIP=info['SERVERIP'],
                    SERVERPORT=info['SERVERPORT'])
                return 'updating is ok!'


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
    # close cursor
    db._db_cursor().close()
    # close connection
    # db._db_cursor().connection.close()


