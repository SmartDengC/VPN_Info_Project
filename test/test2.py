"""
使用suds库测试网上开放webservice接口
"""

from suds.client import Client

user_url="http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl"
#这里是你的webservice访问地址
client=Client(user_url)
#Client里面直接放访问的URL，可以生成一个webservice对象
#print(client)#打印所webservice里面的所有接口方法名称，结果如下截图所示：
ip = '60.205.222.24'
result=client.service.getCountryCityByIp(ip)
#client这个对象 ，调用service这个方法，然后再调用userRegister这个接口函数，函数里面传递刚刚我们准备
#好的得参数字典 t
print(result)#打印返回结果