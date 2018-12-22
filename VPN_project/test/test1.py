import unittest


class MyTest1(unittest.TestCase):
    def test_users_1(self):
        Use = users()

        result = Use.GET()
        for i in range(len(result)):
            print(result[i])
            print('====================')

    # 未完成改方法测试
    def test_users_2(self):
        datas = {
            'USERNAME': 'fly',
            'IDCARD': '510623199752088934',
            'TEL': '18328377763',
            'APPLICANT': 'jet',
            'DEPARTMENT': 'selef',
            'VPNACCOUT': '522222',
            'PASSWORD': '123456',
            'STARTIME': '2018-10-04',
            'ENDTIME': '2018-10-04',
            'ACCTYPE': 'self',
            'SERVERIP': '50.22.20.2',
            'SERVERPORT': '2010',
        }
        Use = users()
        Use.POST()

    def test_user(self):
        Use = user()

        resutl = Use.GET('2')
        print(resutl)




if __name__ == '__main__':

    suit1 = unittest.TestLoader().loadTestsFromTestCase(MyTest1)
    #suit2 = unittest.TestLoader().loadTestsFromTestCase(MyTest2)
    suit = unittest.TestSuite([suit1])
    unittest.TextTestRunner(verbosity=5).run(suit)
    #unittest.main(verbosity=5)
