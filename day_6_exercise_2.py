# # 2. Cubes

# The user enters the beginning (integer) and end number.

# The output is the entered numbers and their cubes

# For example: inputs 2 and 5 (two inputs)

# Output

# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125

# All cubes: [8,27,64,125]


# PS could theoretically do without a list, but with a list it will be more convenient

number_1=int(input("Enter first number: "))
number_2=int(input("Enter second number: "))

make_list=list(range(number_1, number_2+1))

cubes=[]

for num in make_list: 
    cube_single=num**3
    cubes.append(cube_single) 
    print(f"{num} cubed: {cube_single}")  
print(f"All cubed: {cubes}")