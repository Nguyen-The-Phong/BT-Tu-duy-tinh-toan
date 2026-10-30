name=input("Ten chu ho: ")
previous=int(input("Chi so thang truoc: "))
current=int(input("Chi so thang nay: "))
a=current-previous
if a<=50:
    tien=a*1.984
elif a<=100:
    tien=50*1.984 + (a-50)*2.050
elif a<=200:
    tien=50*1.984 + 50*2.050 + (a-100)*2.380
elif a<=300:
    tien=50*1.984 + 50*2.050 + 100*2.380 + (a-200)*2.998
elif a<=400:
    tien=50*1.984 + 50*2.050 + 100*2.380 + 100*2.998 + (a-300)*3.350
else:
    tien=50*1.984 + 50*2.050 + 100*2.380 + 100*2.998 + 100*3.350 + (a-400)*3.460
print(f"Ho va ten: {name}")
print(f"Tien phai tra la: {tien*1080:.0f}")