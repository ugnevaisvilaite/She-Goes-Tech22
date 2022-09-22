# 3. City Population
# The city has a known population p0
# A percentage of population perc is added each year
# Every year a certain number of delta also arrive (or leave)
# We need to know when (if at all) the city will reach a population of p
# Write a function get_city_year (p0, perc, delta, p) that returns the years (full) when p is reached.
# If p cannot be reached, then we return -1
#



# p0 = int(input("Enter city population:"))
# perc = float(input("Enter population percentage added each year:"))
# delta = int(input("Enter number of arrivals(departures):"))
# p = int(input("Enter requested to reach population:"))

# def new_population(p0=0, perc=0, delta=0, full_population=0):
#     percentage = round(perc*0.01,2)
#     full_population = p0+(p0*percentage)+delta
#     return full_population

def get_city_year(p0=0, perc=0, delta=0, p=0):
    percentage = round(perc*0.01,2)
    years=0
    full_population=0
    while full_population < p:
        full_population = p0+(p0*percentage)+delta
        if full_population<=p0:
            return -1
            break
        years +=1
        p0 = full_population
    return years
        
print(get_city_year(1000, 0, -50, 5000))