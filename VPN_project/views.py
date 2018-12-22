import web
from VPN_Info_Project.VPN_project import models, urls


class User:
    # 获取单个用户信息
    @staticmethod
    def GET(USERID):
        USERID = int(USERID)
        data = []
        result = models.select(USERID)
        for i, j in enumerate(result):
            out_j = dict(j)
            data.append(out_j)
        return data

    # 增加
    @staticmethod
    def POST():
        info = web.data()
        info = str(info, encoding='utf-8')
        info = eval(info)
        models.add(info)
        return 'addition is ok!'

    # 修改
    @staticmethod
    def PUT():
        info = web.data()
        info = str(info, encoding='utf-8')
        info = eval(info)
        models.update('USERID', info)
        return 'updating is ok!'

    # 删除
    @staticmethod
    def DELETE():
        models.delete('USERID')
        return 'deletion is ok'


class Users:
    # 获取所有的人员信息
    @staticmethod
    def GET():
        result = models.select_all()
        # result = db.select('todo')
        list_from_db = []
        for menber in result:
            temp = dict()
            for key in menber:
                temp[key] = menber[key]
            list_from_db.append(temp)
        return list_from_db

    # 增加
    @staticmethod
    def POST():
        info = web.data()
        info = str(info, encoding='utf-8')
        info = eval(info)
        models.add(info)
        return 'addition is ok!'

    # 修改
    @staticmethod
    def PUT():
        info = web.data()
        info = str(info, encoding='utf-8')
        info = eval(info)
        models.update('USERID', info)
        return 'updating is ok!'

    # 删除
    @staticmethod
    def DELETE():
        models.delete('USERID')
        return 'deletion is ok'


class Search:
    pass


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
    # close cursor
    # db._db_cursor().close()
    # close connection
    # db._db_cursor().connection.close()


