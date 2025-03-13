import time

timer = int(input("Enter your time: "))

for i in reversed(range(timer)):
    time.sleep(1)
    se = i % 60
    mi = int(i/60)%60
    h = int(i/3600)
    print(f"{h:02}:{mi:02}:{se:02}")

