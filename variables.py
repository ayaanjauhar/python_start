x = 5
y = "John"
print(x)
print(y)
a = 4
a ='Sally' #over writing
print(a)
b = str(3)    # x will be '3'
c = int(3)    # y will be 3
d = float(3)  # z will be 3.0
print(b,c,d)
print(type(c))
print(type(d))
x,y,z = 23,"Sam",7
print(x,y,z,)
x=y=z= 'Orange'
print(x)
print(y)
print(z)
x =str
print(x)
fruits = ['Apple','Banana','Mango']
x,y,z=fruits
print(x,y,z)
x="aj"
y="sam"
print(x + y)
x="aj"
y=707
print(x,y)
h = 'okie'
def myfunc():
    global h
    h = "fantastic"
    print(h)
myfunc()  
print(h)