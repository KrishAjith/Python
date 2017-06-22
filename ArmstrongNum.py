a=input("Enter your Number    : ")
temp1,temp2,temp3,lsum=len(a),int(a),0,0
while(int(temp2)!=0):
    temp3 = int(temp2)%10
    temp2 = int(temp2)/10 
    lsum = lsum + (temp3 ** int(temp1))
if(lsum == int(a)):
    print("\n Armstrong")
else:
    print("\n Not Armstrong")
