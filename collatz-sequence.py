def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number//2
    else:
        if number % 2 == 1:
            result = print(3 * number + 1)
            print(result)
            return result

try:
    number = int(input('Enter a number: '))
    while number != 1:
        print(number)
        number = collatz(abs(number))
except ValueError:
    print('Error:Invalid argument')
    

