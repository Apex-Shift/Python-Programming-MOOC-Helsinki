fahrenheit = int(input("Please type in a temperature (F):"))

celsius = (fahrenheit - 32 ) * 5/9

if celsius > 0:
    print(fahrenheit,"degrees Fahreheit equals",celsius,"degrees Celsius")
if celsius < 0:
    print(fahrenheit,"degrees Fahreheit equals",celsius,"degrees Celsius")
    print("Brr! It's cold in here!")
