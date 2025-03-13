#defining function
def add(a,b):
    t=a+b
    return t
print (add(1,2))

#default vaule if no arg is passed
def f1(a="Sunrise"):
    print(f"Good {a}")
#no arg
f1()

for i in range(5):  # range(5) gives values 0, 1, 2, 3, 4
    f1(i)
