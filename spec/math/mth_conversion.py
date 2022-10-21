########
### math
### conversion
##############

# Temperature Conversion
def celciusToFahrenheit(celcius):
    fahrenheit = int(celcius * (9/5) + 32)
    return f'{celcius}°C = {fahrenheit}°F'

def main():
    print(celciusToFahrenheit(30)) # 30°C = 86°F
    print(celciusToFahrenheit(45)) # 45°C = 113°F
    print(celciusToFahrenheit(20)) # 20°C = 68°F

if __name__ == '__main__':
    main()