first_name = input("Enter your Fast  name : ")
last_name = input("Enter you Last name : ")
age = int(input("Enter the your age : "))
print()
print("-: PERSONAL PROFILE :-")
print("Name : {} {} ".format(first_name,last_name))
print("Age  : {}".format(age))
print()

# Item 1 
item1_name = "NoteBook"
item1_price = 49.0
item1_quantity = 3

item2_name = "keyborad"
item2_price = 199.0
item2_quantity = 2

item3_name = "Mouse"
item3_price = 100.0
item3_quantity = 1

# calculation
subtotal =(item1_price * item1_quantity) + (item2_price * item2_quantity) + (item3_price * item3_quantity)
tax_rate = 0.08 #7% Tax
sales_tax = subtotal * tax_rate
total_bill = subtotal + sales_tax

print(" -: SHOPPING RECEIPT :- ")
print(f"{item1_quantity} x {item1_name:<18}: ${item1_price * item1_quantity: 6.2f}")
print(f"{item2_quantity} x {item2_name:<18}: ${item2_price * item2_quantity: 6.2f}")
print(f"{item3_quantity} x {item3_name:<18}: ${item3_price * item3_quantity: 6.2f}")
print("-" * 30)
print(f"{'Subtotal': <21} : ${subtotal: >6.2f}")
print(f"{'Tax (8%)': <21} : ${sales_tax : >6.2f}")
print("-" * 30)
print(f"{'Total Due ': <21} : ${total_bill : >6.2f}")
print("*********************************")