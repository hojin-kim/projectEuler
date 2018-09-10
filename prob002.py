fibo1 = 1
fibo2 = 1
sum = 0

while(fibo2 < 4000000):
    fibo2 = fibo1 + fibo2
    fibo1= fibo2-fibo1
    if fibo2%2 ==0:
        sum += fibo2
    "print(fibo2)"
    "print(sum)"
    "print()"

print(sum)

"""
on generating we need only three variables; we don't need list. and it's fast. 
"""

sum = 0
list = [1, 1]
n = 0
while(1):
    s = list.__len__()
    n = list[s-1] + list[s-2]
    if n > 4000000:
        break
    list.append(n)

for n in list :
    if n%2 ==0:
        sum += n

print(sum)


"""
or simply we can use list to store all fibo. numbers and then use for loop to have sum of even numbers. 
"""