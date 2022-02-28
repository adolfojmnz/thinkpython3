def readposint(loop=False):
    while True:
        try:
            n = int(input('Positive integer: '))
            if n > 0 and type(n) == int:
                print(f'{n} is a positive integer')
                return # Jumps to finally clause.

            # Raise ValueError if the entered value is not legal.
            raise ValueError

        except KeyboardInterrupt:
            print('\nKeyboardInterrupt signal!')
            return # Ends the process.

        except ValueError:
            print('\nNo legal value was entered!\n')

        finally:
            if loop:
                print('Process cancelled.')
                return # Stops the exception's raises to be printed.

readposint()
