#variable length arg (non keyword arg *args)
#the b would be a tuple
def order_food(a,*b):
    print(f"Minimum Ordered {a}")
    for i in b:
        print(f"You have ordered add-ons: {i}")
    print("Enjoy the food in 10minutes -- delivery in progress")
print(order_food("Pizza","Soup","Wings","Honey-Cake"))

print("========================================================")

#variable length arg **kwargs (keyword arg)
def f2(*a,**b):
    print(a)
    print(b)
f2(10,20,30, s="sandy", work="devops")
