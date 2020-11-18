#   Asking Phase

weight = input("Hello, Please insert your weight:")
weight_unit = input("[L]bs or [K]g ?:")
height = input("Please input your height:")
height_unit = input("[F]eet or [C]entimeters ?:")


#   Converting Weight Phase

if weight_unit.upper() == "L":
    converted_weight = float(weight) * 0.453592
    print("Your weight is", weight, "pounds or ", converted_weight, "kilos")
elif weight_unit.upper() == "K":
    converted_weight = float(weight) * 2.20462
    print("Your weight is", weight, "kilos or ", converted_weight, "pounds")

#   Converting Height Phase

if height_unit.upper() == "F":
    converted_height = float(height) * 30.48
    print("Your height is", height, "or ", converted_height, "Centimeters")
elif height_unit.upper() == "C":
    converted_height = float(height) * 0.0328084
    print("Your height is", height, "or ", converted_height, "Feet")

#   Counting BMI with the Metrical System

if weight_unit.upper() == "K" and height_unit.upper() == "C":
    bmi = (float(weight)  / float(height) / float(height)) * 10000

#   Counting BMI with the Imperial System

if weight_unit.upper() == "L" and height_unit.upper() == "F":
    height = height * 12
    bmi = (float(weight)  / float(height) / float(height)) * 703

#   Your BMI and the Message

if bmi <= 18.5:
    print("Your BMI is", bmi,"You are underweight!")
elif bmi <= 24.9:
    print("Your BMI is", bmi, "Your weight is normal")
elif bmi <= 29.9:
    print("Your BMI is", bmi, "You are overweight!")
elif bmi <= 34.9:
    print("Your BMI is", bmi, "You are obese!")
elif bmi > 24.9:
    print("Your BMI is", bmi, "You are morbedely obese")