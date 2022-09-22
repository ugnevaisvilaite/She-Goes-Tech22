#1. The Big Result
# Write an add_mult function that requires three parameters / arguments
# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest argument value.
# PS Assume that numeric parameters will always be passed to the function, no need to check types
# Various solutions are possible (you are allowed to use other data structures inside function such as list).

# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30
# PSS function should return the result, not print it.



def add_mult(*args):
    number_list = []
    for arg in args:
        number_list.append(arg)
        number_list.sort()
    first_element=number_list[0]
    second_element=number_list[1]
    last_element=number_list[-1]
    # print(first_element, second_element,last_element)
    calc=(first_element+second_element)*last_element
    return calc

print(add_mult(2,2,4,7))