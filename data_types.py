a = "Hello World"	#str
b = 20		#int
c = 20.5		#float
d = 1j		#complex
e = ["apple", "banana", "cherry"]	#list	
f = ("apple", "banana", "cherry")	#tuple
g = range(6)    #range
h = {"name" : "John", "age" : 36}		#dict
i = {"apple", "banana", "cherry"}		#set
j = frozenset({"apple", "banana", "cherry"})		#frozenset
k = True	#bool
l = b"Hello"	#bytes
m = bytearray(5)	#bytearray	
n = memoryview(bytes(5))	#memoryview	
o = None    #nnone type   
print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o, sep="\n")	
aw=3092.2098
print(type(aw))
x= -4+717j
print(type(x))

import random
print(random.randrange(1,103))
s="ciweno090230"
print(len(s))
print("ciw" in s)
print("I am", 18, "years old", sep="")