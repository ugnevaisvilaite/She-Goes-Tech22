# Find and output the first 20 
# (even better option to choose how many first primes we want) 
# prime numbers in the form of a list i.e. [2,3,5,7,11, ...
# so remember we already know how to find a single prime number 
# from previous exercise

 #1 VERSION
    
# prime_range = int(input("Enter how many prime numbers want in your list: "))
# start=int(input("Enter the start number for range: "))
# prime_list=[]
# n=0 #counting number of prime numbers
# while n<prime_range:
#     start+=1
#     count=1
#     for j in range(2,start):
#         if start%j==0: #not prime numbers
#             count=0
#             break
#     if count==1: #prime number
#         prime_list.append(start)
#         n+=1      
# print(prime_list)
        
#2 VERSION - tried with function


prime_range = int(input("Enter how many prime numbers want in your list: "))
start=int(input("Enter the start number for range: "))

def is_prime(number):
    if number == 1:
        return False
    for i in range(2,number):
        if (number % i) == 0:
            return False
    return True
    
    

def get_prime_list(prime_range, start):
    prime_list=[]
    counter=0
    while counter<prime_range:
        if is_prime(start):
            prime_list.append(start)
            counter+=1
        start+=1 
    return prime_list

print(get_prime_list(prime_range, start))
