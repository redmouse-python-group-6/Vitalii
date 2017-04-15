def funck():
	a=1+1
	b=2+3
	print(a+b)

def funck2(a, b):
	print(a+b)

def funck3(x):
	x1=x+12
	return (x1, 1)

def funck4(a=1, b=2):
	return(a/b)

def funck5(*args):
	sum=0
	for i in args:
		sum+=i
	return sum

def funck6(*args, **kwargs):
	"""this funck do nothing"""
	print kwargs


if __name__=="__main__":
	funck()
