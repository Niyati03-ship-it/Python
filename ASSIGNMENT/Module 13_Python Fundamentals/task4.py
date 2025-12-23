#conditional statements
#greater or less

n = int(input("Enter first number: "))
m = int(input("Enter second number: "))

if n>m:
    print(n, " is greaterthan" ,m)
else:
     print(n, " is lessthan" ,m)



#check number is prime or note

n = int(input("Enter a number: "))
count = 0
for i in range (1, n + 1):
    if n%i == 0:
        count+=1
       
if count==2:
    print("prime!!")
else:
    print("not prime!!")



#Grades calculator
name = input("Enter your Name: ")
roll_num = int(input("Enter your Roll Number: "))


print("Enter your Subject Marks")
m1 = int(input("Enter marks of subject1: "))
m2 = int(input("Enter marks of subject2: "))
m3 = int(input("Enter marks of subject3: "))
m4 = int(input("Enter marks of subject4: "))
m5 = int(input("Enter marks of subject5: "))

total_marks = m1+m2+m3+m4+m5
average_marks = (m1+m2+m3+m4+m5)/5

per = total_marks/500*100

print("Total Marks: ", total_marks)
print("Average Marks: ",average_marks)
print("Percentage : ", per)

if per>=90:
    print("Grade          : A+")
elif per>=80 and per<90:
    print("Grade          : A")
elif per>=70 and per<80:
    print("Grade          : B+")
elif per>=60 and per<70:
    print("Grade          : B")
elif per>=50 and per<60:
    print("Grade          : C")
elif per>=40 and per<50:
    print("Grade          : D")
else:
    print("fail")


#check a person is eligible to donate blood 

age = int(input("Enter your age: "))
weight = int(input("Enter your weight in kg: "))

if age >= 18:
    if age <= 60:
        if weight >= 50:
            print("You are eligible to donate blood.")
        else:
            print("You are not eligible to donate blood because your weight is less than 50 kg.")
    else:
        print("You are not eligible to donate blood because you are above 60 years old.")
else:
    print("You are not eligible to donate blood because you are under 18 years old.")