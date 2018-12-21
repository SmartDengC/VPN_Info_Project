import web
import sys
sys.path.append(r"E:\Data_Git\repository_for_github\VPN_info\VPN_Info_Project")


from models import model


urls = (
    '/user/(\d+)', 'user',
    '/users', 'users',
    '/search', 'search'  # 我觉得没有必要，查询所有的用户即可查询所有用户id
)


class user:
    # 获取某个用户的信息
    def __init__(self):
        pass
    # 获取单个用户信息
    def GET(self, USERID):
        USERID = int(USERID)
        datas = []
        result = model.select(USERID)
        for i, j in enumerate(result):
            out_j = dict(j)
            datas.append(out_j)
        return datas

        # 增加
    def POST(self):
        info = web.data()
        info = str(info, encoding='utf-8')
        info = eval(info)
        model.add(info)
        return 'addition is ok!'

    # 修改
    def PUT(self):
        info = web.data()
        info = str(info, encoding='utf-8')
        info = eval(info)
        model.update('USERID', info)
        return 'updating is ok!'

    # 删除
    def DELETE(self):
        model.delete('USERID')
        return 'deletion is ok'


class users():
    # 获取所有的人员信息
    def GET(self):
        result = model.select()
        # result = db.select('todo')
        list_from_db = []
        for menber in result:
            temp = dict()
            for key in menber:
                temp[key] = menber[key]
            list_from_db.append(temp)
        return list_from_db

    # 增加
    def POST(self):
        info = web.data()
        info = str(info, encoding='utf-8')
        info = eval(info)
        model.add(info)
        return 'addition is ok!'

    # 修改
    def PUT(self):
        info = web.data()
        info = str(info, encoding='utf-8')
        info = eval(info)
        model.update('USERID', info)
        return 'updating is ok!'

    # 删除
    def DELETE(self):
        model.delete('USERID')
        return 'deletion is ok'


class search:
    pass

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
    # close cursor
    # db._db_cursor().close()
    # close connection
    # db._db_cursor().connection.close()


