import web
import json
from VPN_Info_Project.VPN_project import models


urls = (
    '/User', 'User',
    '/Users', 'Users',
    '/Search', 'Search'  # 我觉得没有必要，查询所有的用户即可查询所有用户id
)


class User:
    # 获取单个用户信息
    @staticmethod
    def GET():
        args = web.input('USERID')
        USERID = int((args['USERID']))
        data = []
        result = models.select(USERID)
        for i, j in enumerate(result):
            out_j = dict(j)
            data.append(out_j)
        return data

    # 增加
    @staticmethod
    def POST():
        # info = web.data()
        # info = str(info, encoding='utf-8')
        # info = eval(info)
        # models.add(info)
        return 'error'

    # 修改
    @staticmethod
    def PUT():
        info = web.input()
        print(info, type(info))
        # args = eval(web.data())
        # USERID = int(args['USERID'])
        # models.modify(USERID, args)
        return 'updating is ok!'

    # 删除
    @staticmethod
    def DELETE():
        args = web.input('USERID')
        USERID = int((args['USERID']))
        models.delete(USERID)
        return 'deletion is ok'


class Users:
    @staticmethod
    def GET():
        data = []
        result = models.select_all()
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
        args = web.input('USERID')
        USERID = int((args['USERID']))
        info = web.data()
        info = str(info, encoding='utf-8')
        info = eval(info)
        models.update(USERID, info)
        return 'updating is ok!'

    # 删除
    @staticmethod
    def DELETE():
        args = web.input('USERID')
        USERID = int((args['USERID']))
        models.delete(USERID)
        return 'deletion is ok'


class Search:
    @staticmethod
    def GET():
        return 'error'


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()

