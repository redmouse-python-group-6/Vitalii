f=open('tmp.txt')
# for l in f:
# 	print(l)

print(f.read(2))
print(f.tell())
f.seek(0, 0)
print(f.tell())
print(f.read())
f.close()


f=open('tmp.txt', 'w')
for i in [str(x) for x in range(20)]:
	f.writelines(["%s-%s"%(i, int(i)**2), "%s-%s"%(i, int(i)**2)])
f.close()