def funck5(*args):
	sum=0
	for i in args:
		sum+=i
	return sum

def funck6(*args, **kwargs):
	"""this funck do nothing"""
	print kwargs