# 1a. Average value

# Write a program that prompts the user to enter numbers (float).

# number_2=float(input("Enter second number: "))
total=[]

while True:
    number_text=input("Enter first number: ")
    if number_text=="q" :
        print("End")
        break
    else: 
        total.append(float(number_text))
        # sorted_total=sorted(total)
        avg = round(sum(total)/len(total), 2)
        print(avg)


# PS. 1a can do without a list

# 1b. The program shows both the average value of the numbers and ALL the numbers entered

# PS Exit the program  by entering "q"

# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.