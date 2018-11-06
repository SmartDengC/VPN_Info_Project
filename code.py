# -*- coding: utf-8 -*-
import web
import json

#design urls ,there are three urls,ip+port+url
urls =(
    '/addition/data=(.*)', 'addition',
    '/deletion/USERID=(.*)', 'deletion',
    '/revise/USERID=(.*)/data={(.*?)}', 'revise',
    '/users/(.*)', 'users'
)


#抽象数据库连接
class DBconn:
    def conn(self):
        db = web.database(
            dbn='mysql',
            user='root',
            pw='123456',
            db='dbname'
        )
        return db

    def close(self):
        db = DBconn.conn(self)
        #没有 直接关闭数据库的方法
        db.query('exit')


#实现数据的添加
class addition:
    def POST(self, info):
        """
        开始的时候想使用'ip+端口+/+信息的形式'------》》
        然后想传入一个json对象 -------》》
        再后来想传一个 user对象 -----》》
        使用json中嵌入列表，------》》
        还没有更好的想法
        """

        #list = url.split('/')
        db = DBconn.conn(self)
        while type(info) == dict:
            if db.insert(
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
                    SERVERPORT=info['SERVERPORT']):
                return 'ok'
            else:
                return 'error'
    def GET(self,info):
        self.POST(info)


#实现数据的删除
class deletion:
    """根据USERID信息删除"""

    def POST(self, USERID):
        db = DBconn.conn(self)
        if db.delete(
                'todo',
                where='USERID=$USERID',
                vars={
                    'USERID': USERID
                }):

            return 'ok'
        else:
            return 'error'

    def GET(self,USERID):
        self.POST(USERID)


#实现数据的修改
class revise:
    """根据USERID 选中用户，在使用info内的信息修改用户信息"""

    def POST(self, USERID, info):
        db = DBconn.conn(self)
        while type(info)==dict:
            if db.update(
                    'todo',
                    where='USERID=$USERID',
                    vars={
                        'USERID': USERID
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
                    SERVERPORT=info['SERVERPORT']):
                return 'ok'
            else:
                return 'error'
    def GET(self,USERID, info):
        self.POST(USERID,info)

#实现数据的查找
class users:
    """根据USERID 进行查找"""

    def GET(self, USERID):
        datas = [

        ]
        db = DBconn.conn(self)
        if db:
            str = "select *from todo where USERID=%s" %(USERID)
            result = db.query(str)
            for i ,j in enumerate(result):
                #print("i=%s" %(i)) i是索引
                #print("j=%s" %(j)) j是内容
                print("=============!")
                outj = dict(j)
                #datas[i] = outj
                datas.append(outj)
            return datas
        else:
            #print('error')
            return 'error'



if __name__ == '__main__':
    # to get a object called app to web.application
    app = web.application(urls, globals())
    app.run()
