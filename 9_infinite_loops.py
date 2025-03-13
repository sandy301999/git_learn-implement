import time
x = 2
y = 1

while True:
    z = x * y  # Correctly update z as the product of x and y
    print(f"{x} * {y} = {z}\n")
    y += 1  # Increment y for the next iteration
    time.sleep(1)  # Wait for 1 second before the next iteration
