def convert_to_integer(value):
    try:
        result = int(value)
        return result
    except ValueError:
        raise ValueError('Conversion failed. Please enter a valid integer.')
    except Exception as e:
        print(f'An unexpected error occured: {e}')
    else: # Only happens if no exceptions occred
        print('Else invoked')
    finally: # Happens no matter what
        print('Closing any open resources')

# User input
# spam = input('Enter a number to convert to integer: ')
# convert_to_integer(spam)

