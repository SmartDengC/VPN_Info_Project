# -*- coding: utf-8 -*-
import web
import MySQLdb
import MySQLdb.cursors

# to find a model from templates
render = web.template.render('templates') 

#design urls ,there are three urls,ip+port+url
urls=(
	'/index','index',
	'/find','find',
	'/add','add',
	'/delete','delete',
	'/modify','modify'
)



#define class
class index:
	def GET(self):
		return render.index()

class add:
	def GET(self):
		
		return render.add()
	def POST(self):
		i=web.input()
		db = web.database(dbn='mysql', user='root', pw='123456', db='dbname')

		if db.insert('todo',USERNAME=i.USERNAME,IDCARD=i.IDCARD,TEL=i.TELNUM,APPLICANT=i.APPLICANT,DEPARTMENT=i.DEPARTMENT,
VPNACCOUT=i.VPNACCOUT,PASSWORD=i.PASSWORD,STARTIME=i.STARTIME,ENDTIME=i.ENDTIME,ACCTYPE=i.ACCTYPE,SERVERIP=i.SERVERIP,SERVERPORT=i.SERVERPORT):
			return render.true()
		else:
			return render.false()					
		#raise web.seeother('/')
		

class delete:
	def GET(self):
		return render.delete()
	def POST(self):
		
		i=web.input()
		db = web.database(dbn='mysql', user='root', pw='123456', db='dbname')
	
		#if db.delete('todo', where='USERNAME=$USERNAME', vars={'USERNAME':i.USERNAME}):
		if db.delete('todo', where='USERNAME=$USERNAME' and 'SERVERIP=$SERVERIP', vars={'USERNAME':i.USERNAME,'SERVERIP':i.SERVERIP}):
			return render.true()
		else:
			return render.false()
		
class modify:
	def GET(self):
		return render.modify()
	def POST(self):
		i=web.input()
		db = web.database(dbn='mysql', user='root', pw='123456', db='dbname')
		if db.update('todo', where='USERNAME=$USERNAME' and 'SERVERIP=$SERVERIP', vars={'USERNAME':i.USERNAME,'SERVERIP':i.SERVERIP},IDCARD=i.IDCARD,TEL=i.TELNUM,APPLICANT=i.APPLICANT,DEPARTMENT=i.DEPARTMENT,
VPNACCOUT=i.VPNACCOUT,PASSWORD=i.PASSWORD,STARTIME=i.STARTIME,ENDTIME=i.ENDTIME,ACCTYPE=i.ACCTYPE,SERVERIP=i.SERVERIP,SERVERPORT=i.SERVERPORT):
			return render.true()
		else:
			return render.false()
		

class find:
	def GET(self):
		db = web.database(dbn='mysql', user='root', pw='123456', db='dbname')
		#users = db.query('select * from todo where id>$id', vars={'id':100})
		r=db.query('select *from todo')
    		return render.find(r)
		


if __name__ =='__main__':
	# to get a object called app to web.application
	app = web.application(urls, globals()) 
	app.run()
