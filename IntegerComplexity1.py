def divisorFind(n):
    div = []
    for x in range(1,int(n/2+1)):
        if n%x == 0:
            div.append(x)
    smallest = 0
    for index, divisor in enumerate(div):
        if smallest == 0 or smallest > (n/divisor + divisor):
            smallest = (divisor+n/divisor)
    return smallest

print(divisorFind(12345))
