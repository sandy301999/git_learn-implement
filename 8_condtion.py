print("Welcome to Python Course ::::" " This Course has a lot of slides \n" "Find your matching")
python_list = ["Conditions", "Variables", "print format"]
python_tuple = ("NodeJS", "Jupyter Notebook", "Python shell")
python_dic = {"Name": "Python learning", "Skill": "Blockchain", "code": 1234}

usr_input = input("Enter the Python slide: ")
while 1:  # Infinite loop (use with caution)

    if usr_input in python_list:
        print(f"{usr_input} exists in list database")
    elif usr_input in python_tuple:
        print(f"{usr_input} exists in tuple database")
    elif usr_input in python_dic.keys():
        print(f"{usr_input} exists as a key in dictionary database")
    elif usr_input in python_dic.values():
        print(f"{usr_input} exists as a value in dictionary database")
    else:
        print("Doesn't exist in the database")

    # Ask for new input or break the loop
    usr_input = input("Enter another Python slide (or type 'exit' to quit): ")
    if usr_input.lower() == "exit":
        break
