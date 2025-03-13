#Arithmetic operation
from os.path import exists

x = 10
y = 3
t = x + y
a = x - y
b= x/y
print("\n",t,"\n",a,"\n",b)
#to get the remainder
c=x % y
print (c)

#to get the power
b= x**y
print (b)
print ("--------------------------------")

#comparision op
a=11
b=12
t=(a<b)
print (t)
b=10
t=(a==b)
print (t)
t=(a!=b)
print (t)
t=(a>=b)
print (t)
print ("--------------------------------")

#assignment operator
c=1
d=2
c+=d
print (c)
print ("--------------------------------")

#logical operator
a=10
b=20
x=12
y=341

t= (a<b) or (x>y)
print (t)
t= (a<b) and (x>y)
print(t)
t= (a<b) or (x>y)
print(not t)
print ("--------------------------------")

#membership operator
t = ("sandesh", 47, 13324.231, 'sandeshsvsanjana')
#does sandesh exist in this tuple
a= "sandesh" in t
print (a)

a= "sandeshs" not in t
print (a)

a= 47 not in t
print (a)

print ("--------------------------------")

#identity operator
a=15
b=15
t=a is b
print (t)
t = a is not b
print (t)