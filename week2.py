from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, direction):
  end_text = ""
  if direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
      new_char = char
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      if new_position > len(alphabet) - 1:
        new_position -= len(alphabet)
      elif new_position < 0:
        new_position += len(alphabet)
      new_char = alphabet[new_position]
    end_text += new_char

  print(f"Here's the {direction}d result: {end_text}")
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "yes":
    cipher_program()
  else:
    print("Goodbye")

def cipher_program():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % len(alphabet)
  caesar(text, shift, direction)

print(logo)
cipher_program()

#ceil and floor()
#https://www.geeksforgeeks.org/floor-ceil-function-python/


people
= {
 8 "Brian": "+1-617-495-1000"
,
 9 "David": "+1-949-468-2750"
10
}
11
12 # Search for name
13 name
= get_string("Name: "
)
14 if name in people:
15 print
(f"Number:
{people[name]
}
"
)



--------------
from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  
  
  
  https://www.w3schools.com/python/python_strings.asp
    
    
    //////////
    from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()



https://labs.cognitiveclass.ai/tools/jupyterlab/lab/tree/labs/PY0101EN/PY0101EN-2-2-Lists.ipynb?lti=true
