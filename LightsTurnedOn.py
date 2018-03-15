"""There is a light in a room which lights up only when someone is in the room (think motion detector). You are given a
set of intervals in entrance and exit times as single integers, and expected to find how long the light has been on.
When the times overlap, you need to find the time between the smallest and the biggest numbers in that interval."""

with open('inp.txt') as file_object:
    lines = [line.split() for line in file_object]

time = 0
low = int(lines[0][0]) #lower bound
high = int(lines[0][1]) #upper bound
for i in range(len(lines)):
    print(lines[i])
    tmplow = int(lines[i][0])
    tmphigh = int(lines[i][1])
    """What are the possiblies
    1. the tmplow < low and tmphigh < high NONO
    2. the tmplow < low and tmphigh > high NOON
    3. the tmplow > low and tmphigh < high ONNO
    4. the tmplow > low and tmphigh > high ONON"""
    if tmplow < low and tmphigh < high and tmplow <= high and tmphigh >= low:
        low = tmplow
    elif tmplow < low and tmphigh > high and tmplow <= high and tmphigh >= low:
        low = tmplow
        high = tmphigh
    elif tmplow >= low and tmphigh <= high and tmplow <= high and tmphigh >= low:
        time = time
    elif tmplow > low and tmphigh > high and tmplow <= high and tmphigh >= low:
        high = tmphigh
    else:
        time = time + high - low
time = time + high - low
print(time)

