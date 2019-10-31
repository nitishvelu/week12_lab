def mymap(func,itr):
	l=[]
	for i in itr:
		l.append((i,func(i)))
	return l
#defining testing functions
def od_sq(x):
		return x*x
	
def ing_app(str):
	return str+"ing"

list1=["morn","walk","eat","sleep"]

n=int(input(("enter upper limit: ")))

l=[x for x in range(1,n) if x%2]

print(mymap(od_sq,l),"\n")
print(mymap(ing_app,list1),"\n")
print(mymap(len,list1),"\n")


