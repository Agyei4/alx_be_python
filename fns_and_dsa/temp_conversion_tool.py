#
from logging import exception

global FAHRENHEIT_TO_CELSIUS_FACTOR
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

global CELSIUS_TO_FAHRENHEIT_FACTOR
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 31) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

    return fahrenheit


def user_interface():

    try:
        prompt = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("“Invalid temperature. Please enter a numeric value.”")


    prompt_cf = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    if prompt_cf == "f":
        print(f"{prompt}°F is {convert_to_celsius(prompt)}°C")

    elif prompt_cf == "c":
        print(f"{prompt}°F is {convert_to_fahrenheit(prompt)}°F")
    else:
        print("invalid unit")


        return


#test
user_interface()

