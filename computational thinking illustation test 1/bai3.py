elements=input().split()
def compress_consecutive(elements):
    lst=[]
    for k in range(len(elements)):
        if k==0:
            lst.append(elements[k])
        else:
            if elements[k]==elements[k-1]:
                pass
            else:
                lst.append(elements[k])
    return lst

print(compress_consecutive(elements))