#   Preset Phase
bmi = 0                                                                                                                                                                                                                                                                                  
weight_unit = "Not defined yet"
height_unit = "Not defined yet"

#   Asking Phase

print("Hello, would you like to use the Imperial System (Lbs and Feet) or the Metric System (Kg and Cm)?")
unit = input("Please type [I] if you want to use the Imperial System or [M] for the Metric System:")


if unit == "M":
    weight_unit = "K"
    height_unit = "C"
    weight = float(input("Please input your weight in Kilos:"))
    height = float(input("Please input your height in Centimeters:"))
if unit == "I":
    weight_unit = "L"
    height_unit = "F"
    weight = float(input("Please input your weight in Pounds:"))
    height = float(input("Please input your height in Feet:"))


#   Converting Weight Phase

if weight_unit.upper() == "L":
    converted_weight = weight * 0.453592
    print("Your weight is", weight, "pounds or ", converted_weight, "kilos")
elif weight_unit.upper() == "K":
    converted_weight = weight * 2.20462
    print("Your weight is", weight, "kilos or ", converted_weight, "pounds")

#   Converting Height Phase

if height_unit.upper() == "F":
    converted_height = height * 30.48
    height_inches = height * 12
    print(f'Your height is {height} in feet, {converted_height} in centimeters or {height_inches} in inches')
elif height_unit.upper() == "C":
    converted_height = height * 0.0328084
    converted_height_to_inches = height * 0.3937007874
    print(f'Your height is {height} in centimeters, {converted_height} in feet or {converted_height_to_inches} in inches')

#   Counting BMI with the Metrical System

if weight_unit.upper() == "K" and height_unit.upper() == "C":
    bmi = (weight  / height / height) * 10000

#   Counting BMI with the Imperial System

if weight_unit.upper() == "L" and height_unit.upper() == "F":
#    bmi = (float(weight)  / float(height_inches) / float(height_inches)) * 703
#    bmi = (703 * float(weight) / float(height_inches) ** 2)
    bmi = float(converted_weight) / float((converted_height / 100)) ** 2
#   Your BMI and the Message

if bmi == 0:
    print("Sorry, something must have went wrong. Please follow the instructions correctly!")
elif bmi <= 16:
    print(f'Your BMi is {bmi}. \nYou are either extremely underweight, or something went wrong!')
elif bmi <= 18.5:
    print(f'Your BMI is {bmi}. \nYou are underweight!')
elif bmi <= 24.9:
    print(f'Your BMI is {bmi}. \nYou weight is normal')
elif bmi <= 29.9:
    print(f'Your BMI is {bmi}. \nYou are overweight!')
elif bmi <= 34.9:
    print(f'Your BMI is {bmi}. \nYou are obese!')
elif bmi > 24.9:
    print(f'Your BMI is {bmi}. \nYou are morbedely obese')