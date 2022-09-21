# Find and output the first 20 
# (even better option to choose how many first primes we want) 
# prime numbers in the form of a list i.e. [2,3,5,7,11, ...
# so remember we already know how to find a single prime number 
# from previous exercise

    
prime_range = int(input("Enter how many prime numbers want in your list: "))
start=int(input("Enter the start number for range: "))
prime_list=[]
n=0 #counting number of prime numbers
while n<prime_range:
    start+=1
    count=1
    for j in range(2,start):
        if start%j==0: #not prime numbers
            count=0
            break
    if count==1: #prime number
        prime_list.append(start)
        n+=1      
print(prime_list)
        
