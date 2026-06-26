#program to create quiz application.
print("==== Quiz Application ====")
name = input("Enter your name:")
print ("start the quiz!")
score = 0

#question 1
print("1. What is the capital of India?")
print("a. Mumbai")
print("b. New Delhi")
print("c. Kolkata")
print("d. Chennai")
ans = input("Enter your answer. (a/b/c/d):")
if ans == "b":
    print("correct!")
    score +=1
else :
    print("Incorrect ! correct answer is b New Delhi. ")

#question 2
print("2. What is the national bird of India ?")
print("a. Parrot")
print("b. Crow")
print("c. Peacock")
print("d. Owl")
ans = input("Enter your answer. (a/b/c/d):")
if ans == "c":
    print("correct!")
    score +=1
else :
    print("Incorrect ! correct answer is c Peacock.")

#question 3
print("3. What is the national animal of India?")
print("a. Tiger")
print("b. Elephant")
print("c. Lion")
print("d. Horse")
ans = input("Enter your answer. (a/b/c/d):")
if ans == "a":
    print("correct!")
    score +=1
else :
    print("Incorrect ! correct answer is a Tiger. ")

#resul
print("==== Quiz Result ====")
print("Your score",score,"/3")
if score == 3:
    print("Excellent! ",name," you got all answers correct.")
elif score == 2:
    print("Very good!",name)
elif score == 1:
    print("Good!",name," keep practicing.")
else :
    print("Better luck next time!",name)