# 1. Health check

# Ask user for their temperature.

temp = int(input ("What us your temperature?"))

# If the user enters below 35, then output "not too cold"
if temp < 35 :
    print ("Your temperature is not too cold")

elif temp <= 37 :
    print ("Your temperature is alright")
# If 35 to 37 (inclusive), output "all right"
else :
    print ("You possibly have fever")
    # If the temperature  over 37, then output  "possible fever

# remember about type conversion if needed