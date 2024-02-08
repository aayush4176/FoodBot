print("Welcome to FoodBot!")

name = input("What is your name? ")
age = input("What is your age? ") 

print(f"Hi {name}!")

print("How can I help you today?")
print("1. My food order hasn't arrived")
print("2. I received the wrong order") 
print("3. Speak to an staff member")
print("4. Exit conversation")

choice = input("Please enter your choice (1/2/3/4): ")

if choice == "1":
  order_number = input("Please provide your order number: ")
  print(f"I apologize your order {order_number} has not arrived yet. I will contact the restaurant and delivery driver to expedite your order.")

elif choice == "2":
  order_number = input("Please provide your order number: ")
  print(f"I apologize you received the wrong order for order {order_number}. I will contact the restaurant to arrange a replacement order to be delivered to you.")

elif choice == "3":
  print("Connecting you to an staff member...")

elif choice == "4":
  print("Thank you for using FoodBot. Have a great day!")
  exit()

else:
  print("Invalid choice")

print("Thank you for using FoodBot. Have a great day!")