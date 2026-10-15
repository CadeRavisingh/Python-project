def celsius_to_fehrenheit(celsius):
    return (celsius * (9/5)) + 32
def fehrenheit_to_celsius(fehrenheit):
    return (fehrenheit -32 ) *(9/5)
def km_to_mile(km):
    return km*0.621371
def mile_to_km(mile): 
    return mile/0.621371
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("please enter vaild input : ")
def main():
    while True:
       print("1.Celsius to Fehrenheit  ")
       print("2.Fehrenheit to Celsius  ")
       print("3.Kilometer to Miles  ")
       print("4.Miles to Kilometer ")
       print("5.Exit")

       choice = input("Choice an Option (1-5 ): ").strip()
       if choice == '1':
           c = get_float_input("Enter the Temperature in Celsius : ")
           print(f"{c}C = {celsius_to_fehrenheit(c):.2f}F")
       elif choice == '2':
           f = get_float_input("Enter the Temperature in Fehrenheit : ")
           print(f"{f}F = {fehrenheit_to_celsius(f):.2f}C")
       elif choice == '3':
           k = get_float_input("Enter the Distance  in Km : ")
           print(f"{k} Km = {km_to_mile(k):.2f} Miles")
       elif choice == '4':
           m = get_float_input("Enter the Distance in Miles : ")
           print(f"{m} Miles = {mile_to_km(m):.2f} Km")
       elif choice == '5':
           print(" Good Byee thank you for using converter. ")
           break
       else :
           print("'Invalid choice ' please enter the number between 1 to 5 ")
    
if __name__=='__main__':
    main()