import math
a,b,c=map(int,input().split())
p=(a+b+c)/2
if a+b>c and a+c>b and b+c>a:
    print(f"{math.sqrt(p*(p-a)*(p-b)*(p-c))}")
else:
    print("Khong phai 3 canh cua tam giac")
    # cos the dung raise ValueError