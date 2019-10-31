"""
Write a function mymap which takes a callback and an iterable, creates a list,
applies the callback to each element of the iterable and puts the result into
list and returns the list. mymap should mimic map.
Test this with the following calls.
a)Create a list of square of odd numbers from 1 to n.
b)Given a list of words, return a list of words with ing appended to it.
my_list = ['morn', 'walk', 'eat', 'sleep']
c)Given a list of words, return a list of tuples having the word and its length.
my_list = ['morning', 'walk', 'eat', 'sleep']
"""
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


