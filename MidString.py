a=input("Enter your String    :  ")
i=int(len(a)/2)
a=list(a)
a[i]='*'
temp1=''.join(a)
print(temp1)
print(temp1[::-1])
