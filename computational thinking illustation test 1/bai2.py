n=int(input())
def sum_even_digits(n: int):
    sm=0
    while True:
        a=n%10
        if a%2==0:
            sm+=a
        n=n//10
        if n==0:
            break 
    return sm

print(sum_even_digits(n))