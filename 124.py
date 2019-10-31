"""
Write a function to mimic reduce - called myreduce.
Test this with the following calls.
a) Given a list of numbers, find maximum in the list.
l = [23,45,12,47,54]
b) Given a list of integers, combine all integers to form a single integer.
l = [23,45,12,47,54]
"""
def my_reduce(func,itr):
	x=itr[0]
	for item in itr[1:]:
		x=func(x,item)
	return x
#test variable
l=[23,45,12,47,54]
print(my_reduce(max,l))
print(my_reduce(lambda x,y:str(x)+str(y),l))


