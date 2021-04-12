number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
  print(f"it's a even number")
else:
  print(f"its odd")

  /////////////////
  
  import random

coin= ["head", "tails", "bruno", "hello"]
print(random.choice(coin))

////////////////////
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random 

whoWillPay = random.choice(names)
print(whoWillPay)

////////////////

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

#adding new itens
programming_dictionary['hello'] = "olá"

print(programming_dictionary)
