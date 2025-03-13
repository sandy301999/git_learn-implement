import random

# List of vaccines
vaccines = ["Covishield", "Sputnik", "Pfizer", "Moderna", "Janssen"]

# Shuffling the list of vaccines
random.shuffle(vaccines)
print(vaccines)

# Selecting a random vaccine for testing
selected_vaccine = random.choice(vaccines)


# Testing each vaccine
for i in vaccines:
    print(f"Testing vaccine: {i}")
    if i == selected_vaccine:
        print(f"Vaccine {i} passed the test successfully, stopping further tests.")
        print("===================")
        continue
    print("XXXXXXXXXXXX\n","Test failed\n","XXXXXXXXXXXX")


