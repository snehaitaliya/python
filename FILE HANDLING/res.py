# Open file in append mode
f = open("std.txt", "a")

# Input
roll = int(input("Enter Roll No. : "))
name = input("Enter Name : ")

s1 = int(input("Enter Marks Of S1 : "))
s2 = int(input("Enter Marks Of S2 : "))
s3 = int(input("Enter Marks Of S3 : "))
s4 = int(input("Enter Marks Of S4 : "))
s5 = int(input("Enter Marks Of S5 : "))

# Calculation
total = s1 + s2 + s3 + s4 + s5
avg = total / 5

print("Total :", total)
print("Average :", avg)
print("Max :", max(s1, s2, s3, s4, s5))
print("Min :", min(s1, s2, s3, s4, s5))

# Grade
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 33:
    grade = "D"
else:
    grade = "Fail"

print("Grade :", grade)

# Result
cnt = 0

if s1 < 35:
    cnt += 1
if s2 < 35:
    cnt += 1
if s3 < 35:
    cnt += 1
if s4 < 35:
    cnt += 1
if s5 < 35:
    cnt += 1

if cnt == 0:
    result = "Pass"
elif cnt <= 2:
    result = "ATKT"
else:
    result = "Fail"

print("Result :", result)

# Write data into file
f.write(f"{roll}\t{name}\t{s1}\t{s2}\t{s3}\t{s4}\t{s5}\t{total}\t{avg:.2f}\t{grade}\t{result}\n")

# Close file
f.close()

print("Student Record Saved Successfully.")