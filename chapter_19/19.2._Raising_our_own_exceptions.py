def get_age():
    age = int(input('Please enter your age: '))
    if age < 0:
        # Create a new instance of an exception.
        error = ValueError(f'{age} is not a valid age')
        raise error
    return age

if __name__ == '__main__':
    print(get_age())

