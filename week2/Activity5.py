#Author: Sanjeev kumar
#Temperature converter

def fahrenheit_to_celsius(f_temp): 
    return (f_temp - 32) * 5 / 9

def celsius_to_fahrenheit(c_temp):
    return (c_temp * 9 / 5) + 32

def temperature_converter():
    user_input = input("Enter temperature to convert: ")

    if len(user_input) < 2:
        print("Invalid input. Please enter the temperature with the correct 'C' or 'F'.")
        temperature_converter()
        return

    prefix = user_input[-1].upper()
    value_part = user_input[:-1]

    # Check if the value part is a number
    if not value_part.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter the temperature with the correct 'C' or 'F'.")
        temperature_converter()
        return

    temp_value = float(value_part)

    if prefix == 'F':
        converted = round(fahrenheit_to_celsius(temp_value), 2)
        print(f"{user_input} degrees Fahrenheit is converted to {converted} degrees Celsius")
    elif prefix == 'C':
        converted = round(celsius_to_fahrenheit(temp_value), 2)
        print(f"{user_input} degrees Celsius is converted to {converted} degrees Fahrenheit")
    else:
        print("Invalid input. Please enter the temperature with the correct 'C' or 'F'.")
        temperature_converter()

# Run the converter
temperature_converter()
