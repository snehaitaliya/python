rollno=input("enter roll no. : ")
name=input("enter name : ")
s1=int(input("enter marks s1 = "))
s2=int(input("enter marks s2 = "))
s3=int(input("enter marks s3 = "))
s4=int(input("enter marks s4 = "))
s5=int(input("enter marks s5 = "))

print("roll no. : ",rollno)
print("name : ",name)
print("s1 = ",s1)
print("s2 = ",s2)
print("s3 = ",s3)
print("s4 = ",s4)
print("s5 = ",s5)

if s1>s2 and s1>s3 and s1>s4 and s1>s5:
    print("s1 is max",s1)
elif s2>s3 and s3>s4 and s4>S5:
    print("s2 is max",s2)
elif s3>s4 and s4>s5:
    print("s3 is max",s3)
elif s4>s5:
    print("s4 is max",s4)
else:
    print("s5 is max",s5)

if s1<s2 and s1<s3 and s1<s4 and s1<s5:
    print("s1 is min",s1)
elif s2<s3 and s3<s4 and s4<S5:
    print("s2 is min",s2)
elif s3<s4 and s4<s5:
    print("s3 is min",s3)
elif s4<s5:
    print("s4 is min",s4)
else:
    print("s5 is min",s5)

total=s1+s2+s3+s4+s5
per=total/5

print("total = ",total)
print("per = ",per)


    
if per>90:
    print("grade A")
elif per>70:
    print("grade B")
elif per>50:
    print("grade c")
elif per>35:
    print("grade D")

cnt=0

if s1<35:
    cnt+=1
elif s2<35:
    cnt+=1
elif s3<35:
    cnt+=1
elif s4<35:
    cnt+=1
elif s5<35:
    cnt+=1
else:
    cnt=0

if cnt==0:
    print("pass")
elif cnt>=1:
    print("ATKT")
else:
    print("fail")


    
    
