# https://docs.python.org/3/library/functions.html
# https://www.geeksforgeeks.org/python-built-in-functions/

message="corona vaccine is ready to use, most of them are more than 90% effective."
print(message,"\n")
print(message.capitalize(),"\n")


#dir function to print all the available function for this message
print(dir(message),"\n")
print(dir([]),"\n")

#all upper case
print(message.upper())

#to check if all are in upper/lower case
print(message.islower())
print(message.isupper())

#print the line where it starts
print(message.find("ready"))

print(message[18:24])

#string joining
txt=("192","168","12","24")
print(".".join(txt))

#append at the end
city=["CTA","BNG","CHK","MLR"]
print(city)
city.append("Del")
print(city)

#extend with own list
city.extend(["Hehe","Hi"])
print(city)

#insert at a postion
city.insert(2,"Insert at 2")
print(city)

#poping out the list from last
city.pop()
print(city)

city.pop(5)
print(city)