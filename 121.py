
"""Given a list of strings:
1)find all strings starting with a given prefix.
2) find all strings having a given substring.
"""
#sample list x
x=["god","pod","mood","good","lol"]
l=list(filter(lambda i:i.startswith("go"),x))
print(l)
s=list(filter(lambda i:"o" in i,x))
print(s)
