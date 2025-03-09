def convert(number, choice):
    if choice == 'f':
        result = number - 32 * (5/9)
    elif choice == 'c': 
        result = number * (9/5) + 32
    print(result)

temperature = input('Do you want to convert :\na) Farenheit to Celcius\nb) Celcius to Farenheit\n>> ') 
number = float(input('What is the temperature you want to convert?\n>>'))

f_to_c = ['Farenheit to Celcius', 'a', 'a)']
c_to_f = ['Celcius to Farenheit', 'b', 'b)']

if temperature in f_to_c:
    convert(number, 'f')
elif temperature in c_to_f:
    convert(number, 'c')

