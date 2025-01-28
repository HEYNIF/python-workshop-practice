day_of_week = input("Enter the day of week: " ).lower()
print(day_of_week)

if day_of_week == "satuday" or day_of_week == "sunday":
    print("I will learn devops live")
else:
    print("I will practice devops")


num1 = int(input("enter the first no: "))
num2 = int(input("enter the second no: "))

choice = input("Enter your choice (Options +, -, *, /, %)")

if choice == '+':
    sum_of_num = num1 + num2
    print('addition',sum_of_num)
elif choice == "-":
    dif_of_num = num1 - num2
    print('subtraction',dif_of_num)
elif choice == "*":
    pro_of_num = num1 - num2
    print('Multiply',pro_of_num)
elif choice == "/":
    div_of_num = num1 - num2
    print('divide',div_of_num)
elif choice == "%":
    rem_of_num = num1 - num2
    print('remainder',rem_of_num)
else:
    print("Invalid choice")


