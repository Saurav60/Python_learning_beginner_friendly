def add_two_numbers():
    try:
        a = input('enter first number: ').strip()
        if not a:
            raise ValueError('first number is missing.')
        a = int(a)
        b = input('enter second number: ').strip()
        if not b:
            raise ValueError('second number is missing.')
        b= int(b)
        
        result = a+b
        print(f'the sum of {a} and {b} is: {result}')
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'an unexpected error occured: {e}')
add_two_numbers()