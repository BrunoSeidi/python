print("Hello world")
print("Day 1 - String Manipulation")
print("String Concatenation is done with the '+' sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


## 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
  if year % 100 ==0:
    if year % 400 == 0:
       print("leap year")
    else:
      print("not leap year")
  else:
    print("leap year")
else:
  ("not")
