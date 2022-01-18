# Split string method
import random
print("The person selected will have to pay for everybody's food bill.")
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
print("List of the person who will going toh pay the money ",names)
name=len(names)
print("How many people are participating in deposit money= ",name)
random=random.randint(0,name-1)
print("Number of the person who will pay= ",random)
person_name=names[random]
print("the peson name who will pay money= ",person_name)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇



