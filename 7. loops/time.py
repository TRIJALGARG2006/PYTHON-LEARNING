import time 
mytime = int(input("Enter your time in seconds:"))

for x in range(mytime, 0 ,-1):
    sec = x % 60
    min = int(x / 60) % 60
    hours = int(x /3600)
    print(f"{hours}:{min:02}:{sec:02}")
    time.sleep(1)
print("time up")