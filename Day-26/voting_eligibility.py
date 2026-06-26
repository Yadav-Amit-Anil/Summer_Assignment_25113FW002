#program to create voting eligibility system.
print("====Voting Eligibility System====")
name = input("Enter your name:")
age = int(input("Enter your age:"))
citizenship = input("Are you an Indian citizen? (yes?no):")
voter_id = input("Do you have voter ID (yes?no):")
if age < 0 or age > 120:
    print("Invalid age entered.")
elif age <18:
    print("You are not eligible to vote because you are below 18:")
elif citizenship == "no" :
    print("You are not eligible for voting because you are not indian.")
elif voter_id == "no":
    print("You are not eligible for votimg because you don't have voter ID")
else:
    print("Congratulations!",name)
    print("You are eligible for voting.")