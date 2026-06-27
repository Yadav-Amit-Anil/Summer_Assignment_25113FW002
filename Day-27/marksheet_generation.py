#program to create marksheet generation system
print("===== Marksheet Generation System =====")

name = input("Enter student's name:")
roll = input("Enter student's roll number")

sub1 = int(input("Enter marks of english:"))
sub2 = int(input("Enter marks of maths:"))
sub3 = int(input("Enter marks of science:"))
sub4 = int(input("Enter marks of social:"))
sub5 = int(input("Enter marks of hindi:"))

marks = sub1 + sub2 + sub3 + sub4 + sub5
percent = marks/5

if percent > 90:
    grade ="A+"
elif percent > 80 and percent < 90:
    grade = "A"
elif percent > 70 and percent < 80:
    grade = "B"
elif percent > 60 and percent < 70:
    grade = "C"
elif percent > 50 and percent < 60:
    grade = "D"
else:
    grade = "Fail"

print("==== Marksheet ====")
print("Name:",name)
print("Roll number:",roll)
print("==== Marks Obtained ====")
print("English=",sub1)
print("Maths=",sub2)
print("Science=",sub3)
print("Social=",sub4)
print("Hindi=",sub5)
print("------------------------")
print("Total marks=",marks)
print("Percentage Obtained=",percent,"%")
print("Grade=",grade)
