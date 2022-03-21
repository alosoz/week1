# 3.Body Mass Index Calculator
# Parameter showing whether a person's weight is normal for their height. 
# It is called Body Mass Index. In short, a person's weight is equal to a person's height. 
# If we divide it by its square, the body mass index is obtained. User's weight and height. 
# If the result by taking the length is below 25, NORMAL, if it is between 25-30 OVER WEIGHT, 
# OBSE if 30-40, EXTREMELY OBSE if 40 and over print a warning.

weight = int(input("Your Weight : "))
height = int(input("Your Height : "))

IBM = weight/height**2

if IBM < 25:
    print("NORMAL")
elif IBM < 30:
    print("OVER WEIGHT")
elif IBM < 40:
    print("OBESE")
elif IBM >= 40:
    print("EXTREMELY OBESE")