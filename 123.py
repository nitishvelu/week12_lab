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