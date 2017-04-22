class User():
	name=""
	snanme=''
	age=0

	def __init__(self, name, sname):
		self.height=180
		self.name=name
		self.sname=sname
		self.say_hello()

	def __repr__(self):
		return "%s %s"%(self.sname, self.name)

	def olde(self):
		self.age+=1

	@staticmethod
	def say_hello(name='MR'):
		print 'Hello %s'%name

	@classmethod
	def say_name(cls):
		print 'My name is %s'%cls.name

	def __del__(self):
		print("GoodBay!!!")