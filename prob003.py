import gmpy2

thenumber = 600851475143
prime = 2
answer = 0
while thenumber > 1:
    if thenumber % prime == 0:
        thenumber = thenumber/prime
        continue
    prime = gmpy2.next_prime(prime)
    answer = prime
print(answer)

""" 
gmpy2 에 있는 next_prime 을 썼음. 다음에 소수에 대한 함수들을 만들어봅시다요  
"""