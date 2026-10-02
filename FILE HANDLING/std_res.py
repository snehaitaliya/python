f=open("std.txt","a")

roll=int(input("Enter Roll No. : "))
name=input("Enter Name : ")
s1=int(input("Enter Marks Of S1 : "))
s2=int(input("Enter Marks Of S2 : "))
s3=int(input("Enter Marks Of S3 : "))
s4=int(input("Enter Marks Of S4 : "))
s5=int(input("Enter Marks Of S5 : "))

total=s1+s2+s3+s4+s5
avg=total/5
print("Total : ",total)
print("Average : ",avg)

m=max(s1,s2,s3,s4,s5)
mi=min(s1,s2,s3,s4,s5)

if avg>90:
    Grade="A"
elif avg>80:
    Grade="B"
elif avg>60:
    Grade="C"
elif avg>=33:
    Grade="D"
else:
    Grade="Fail"

cnt=0
if s1<35:
    cnt+=1
if s2<35:
    cnt+=1
if s3<35:
    cnt+=1
if s4<35:
    cnt+=1
if s5<35:
    cnt+=1

if cnt==0:
    result="Pass"
elif cnt<=2:
    result="ATKT"
else:
    result="Fail"

if f.tell()==0:
    f.write(f"Roll\tName\tS1\tS2\tS3\tS4\tS5\tMin\tMax\tTotal\tPer\t  Grade\tResult\n")
f.write(f"{roll}\t\t{name}\t{s1}\t{s2}\t{s3}\t{s4}\t{s5}\t{mi}\t{m}\t{total}\t\t{avg}\t{Grade}\t{result}\n")



