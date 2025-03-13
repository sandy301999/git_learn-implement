str2 = "hi my name is sandy"
str1 = "alpha is beta and beta is the gamma hehehehe"
print (str1[0], str1[1])
print (str1[-1], str1[-2])

#slicing a string [start range: end range]
print(str1[0:5])
print(str1[0:])
print(str1[:5])
print(str1[:])
print ("-----------------------------------")
first_list = [str1, "sandesh", 47]

first_tuple = (str2, "sandesh", 47, 123.345)
print(first_tuple[0],"\n")
print(first_tuple[0][-5:])
print(first_tuple[0][-1:-6:-1])
print ("-----------------------------------")


first_dict = {"Course":("AWS", "Jenkins", "Ansible"), "development":["Java","fullstack","support"]}
print(first_dict)
print(first_dict["Course"])
print(first_dict["development"])
print(first_dict["Course"][-1])
print(first_dict["Course"][-1][0:4])