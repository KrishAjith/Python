a=int(input("Enter your Number   :  "))
temp1,temp2,Num=0,0,a
while(a!=0):
    temp1 = int(a%10)
    a =int(a/10)
    temp2 = temp1  + temp2
print("\nSum of",Num,"is   :",temp2)
