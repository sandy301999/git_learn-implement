import time
x = 2
y = 1
while True:
    z = x * y  #skips when y=5 and goes to while starting to execute next
    if y == 5:
        y+=1
        continue
    print(f"{x} * {y} = {z}")
    y += 1  # Increment y for the next iteration
    time.sleep(.2)  # Wait for 1 second before the next iteration
    if y>10:
        break