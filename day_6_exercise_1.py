# 1a. Average value

# Write a program that prompts the user to enter numbers (float).
number_text=input("Enter first number: ")
# number_2=float(input("Enter second number: "))
make_list=[]
(number_text.split(","))

while True:
    if number_text=="q" :
        print("End")
        break
    else: 
        single=number_text.split(",")
        make_list.append(single)
    avg = round(sum(make_list)/len(make_list), 2)
    print(avg)


# PS. 1a can do without a list

# 1b. The program shows both the average value of the numbers and ALL the numbers entered

# PS Exit the program  by entering "q"

# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.