numlist = range(1, 1000)
sum = 0
newlist = [number for number in numlist if number % 3 == 0 or number % 5 == 0]
for m in newlist:
    sum += m
print(sum)

""" 
파이썬 list
range(시작 정수, 끝정수+1)

for i in list : 
    어쩌고
    저쩌고 

newlist = [ f(n) for n in (list) if (condition) ] : list 에 있는 n 이 condition 을 만족할 때마다 f(n) 으로 리스트 만들기

233168

"""