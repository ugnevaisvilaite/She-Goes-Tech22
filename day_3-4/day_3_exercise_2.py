# 2. Xmas Bonus

# The company has promised a Christmas bonus in the amount of 15% of the monthly salary for EVERY year of 
# service over 2 years.

# Task. Ask the user for the amount of the monthly salary and the number of years worked.
salary = float(input ("What is your monthly salary? "))
years = float(input ("How many years you worked in this company ?"))

years_min = 2
bonus = 0.15
# Calculate the bonus.
if years > years_min:
    bonus_amount = round(((years - years_min) * salary * bonus),3)
    print(f"Your Christmas bonus this year will be {bonus_amount}!")
          
else:
    print ("Sorry no bonus, maybe next year")
    # Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.

# Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0)