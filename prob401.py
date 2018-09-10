import gmpy2
from gmpy2 import mpz
import math

input = (10**6)/2 -1
mod = 10**9
def sqrsum(n):
    n = math.floor(n)
    return n*(n+1)*(2*n+1)//6

sinput = math.floor(math.sqrt(input))

def ans(number) :
    snum = math.floor(math.sqrt(number))
    sum = 0
    "// sinput 까지만 이 합을 수행함"
    for i in range(1, snum + 1):
        sum = (sum + i*i* (number//i) )% mod


    k = math.floor(number/snum)-1
    ind = snum
    temp = 0
    while k!= 0 :
        sum += k* (sqrsum((number/k)) - sqrsum(ind))
        sum = sum % mod
        ind = math.floor(number / k)
        k = k - 1

    return sum

def sigma2 (number):
    return ans(number) - ans(number-1)

print( ans (1000000000000000))


"""
We can handle very very big integers in python; to do this, we have to make sure that we are dealing with "integers". 
ex. num1/num2 는 실수형 출력이 되고 num1//num2 는 정수형 출력이 됨. (몫만 계산)  
"""

#for k in range(20000, 200000):
#    print("%d, %d, %d, %d" %(k, sigma2Mod(k), sigma2(k), sigma2Mod(k)- sigma2(k)))

"""
Problem :
The divisors of 6 are 1,2,3 and 6.
The sum of the squares of these numbers is 1+4+9+36=50.

Let sigma2(n) represent the sum of the squares of the divisors of n. Thus sigma2(6)=50.
Let SIGMA2 represent the summatory function of sigma2, that is SIGMA2(n)=∑sigma2(i) for i=1 to n.
The first 6 values of SIGMA2 are: 1,6,16,37,63 and 113.

Find SIGMA2(1015) modulo 109.
====== 
Consider
SIGMA2(6)   = sigma2(1) + sigma2(2) + sigma2(3) + sigma2(4) + sigma2(5) + sigma2(6)
            = 1^2       + 1^2       + 1^2       + 1^2       + 1^2       + 1^2
                        + 2^2                   + 2^2                   + 2^2  
                                    + 3^2                               + 3^2
                                                + 4^2
                                                            +5^2
                                                                        + 6^2
            = 1^2 * floor[6/1] + 2^2 * floor(6/2) + 3^2 * floor(6/3) + 
            4^2 * floor(6/4) + 5^2 * floor(6/5) + 6^2 * floor(6/6)  

it is simply changing the order of the double summation.
Now we can do this with big numbers.. but still the loop is too big. 
but we can manage this loop; see the 3^2, 4^2, 5^2, 6^2 in the above example: they don't appear that much 
and further : the number they appear is same in some intervals : in this example, we can truncate it as [3], [4, 5, 6]
Using this, the complexity is bigO(input^0.5) and it is computable within a minute. 
                                                      
"""


"""
First, I tried to compute sigma2 functions uising the multiplicative property; but 
the loop is too big to do it all. 
My try below: 

def primePwr(num, prime):
    ind = 0
    temp = num
    while temp % prime == 0:
        ind += 1
        temp = temp / prime
    return ind

def primeFactorsList(num):
    plist = []
    prime = 2;

    while prime *2 < num +1:
        if num%prime ==0 :
            plist.append(prime)
            for i in range(primePwr(num, prime) ):
                num = num / prime
        prime = gmpy2.next_prime(prime)

    if gmpy2.is_prime(mpz(num)):
        plist.append(num)
    return plist


def sigma2primeMod(prime, power):
    return (prime**(2 * power+2) -1)/ (prime*prime -1)



def sigma2Mod(num):
    prod  = 1
    mylist = primeFactorsList(num)
    temp = 0
    for p in mylist:
        ind =0
        temp = num
        while temp%p == 0 :
            ind += 1
            temp = temp/p
        prod *= sigma2primeMod(p, ind)
        prod = prod%1000000000

    return prod

ans = 0
for i in range(1, 1000000000000000+1) :
    ans += sigma2Mod(i)
    if( i % 1000000):
        print("%d000000 step"%i)
print(ans)

"""