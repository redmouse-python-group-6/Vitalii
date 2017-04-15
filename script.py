def funck():
	a=1+1
	b=2+3
	print(a+b)

funck()
funck()

def funck2(a, b):
	print(a+b)

funck2(1, 2)
# x=int(raw_input('Input x\n'))
x=1
r=funck2(x, x)
print(r)

def funck3(x):
	x1=x+12
	return (x1, 1)

w=funck3(x)
print(w)
funck2(x, x)

def funck4(a=1, b=2):
	return(a/b)

print(funck4())
print(funck4(b=float(2)))

def funck5(*args):
	sum=0
	for i in args:
		sum+=i
	return sum

print(funck5())
print(funck5(1))
print(funck5(1,23,4,5,6,7,8,8,9))	

def funck6(*args, **kwargs):
	"""this funck do nothing"""
	print kwargs

funck6(12121, 3, i=1,b=2)
print(funck6.__doc__)
print(len.__doc__)