print("VOTING QUALIFICATION \n")

input("Please enter your name: " "\n")

age = int(input("Please enter your age: " "\n"))
if age>=18:
    print("Congratulations! You are qualified for voting. ""\n") 
    quit()
else:
    print("Sorry you are not accepted to participate in voting until you reach 18 years ")
    quit()
