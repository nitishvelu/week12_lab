"""
Write a function to mimic filter - called myfilter.
Test this with the following calls.
1) Given a list of strings, remove all strings having first character as digit.
l = ["hi","1gff","h3445","6sds","dfdg","234234"]
"""
def my_filter(func,itr):
	l=[]
	for i in itr:
		if func(i):
			l.append(i)
	return l
#test function
def test(str):
	if str[0].isdigit():
		return False
	else:
		return True
#test variable
l=["hi","gi","h3445","dfdg","2345","nitish"]

print(my_filter(test,l))