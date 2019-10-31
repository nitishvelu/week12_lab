def my_reduce(func,itr):
	x=itr[0]
	for item in itr[1:]:
		x=func(x,item)
	return x
#test variable
l=[23,45,12,47,54]
print(my_reduce(max,l))
print(my_reduce(lambda x,y:str(x)+str(y),l))


