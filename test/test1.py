import code
import unittest
import requests
import json
from code import *


class MyTest1(unittest.TestCase):
    def testAddition(self):

        addi = code.addition()
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

        if addi.GET(datas) != 'error':
            print('succeed!--->1')
        else:
            print('error-->>1')


class MyTest2(unittest.TestCase):
    def testDeletion(self):
        dele = code.deletion()
        if dele.GET(11) != 'error':
            print('succeed!--->2')
        else:
            print('error--->>2')


class MyTest3(unittest.TestCase):
    def testRevise(self):
        rev = code.revise()
        datas = {
            'USERNAME': 'wudf',
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
        if rev.GET(10, datas) != 'error':
            print('succeed!---->3')
        else:
            print('error---->>3')


class MyTest4(unittest.TestCase):
    def testUsers(self):
        ins = code.users()
        if ins.GET(2) != 'error':
            print('succeed!------>4')
            for i in ins.GET(1):
                print(i)
        else:
            print('error---->>4')


if __name__ == '__main__':

    suit1 = unittest.TestLoader().loadTestsFromTestCase(MyTest1)
    suit2 = unittest.TestLoader().loadTestsFromTestCase(MyTest2)
    suit3 = unittest.TestLoader().loadTestsFromTestCase(MyTest3)
    suit4 = unittest.TestLoader().loadTestsFromTestCase(MyTest4)
    suit = unittest.TestSuite([suit1,suit2,suit3,suit4])
    unittest.TextTestRunner(verbosity=5).run(suit)
    #unittest.main(verbosity=5)
