def run_apple_guessing_game(target):
    while True:
        guess = int(input('Guess How Many Apples I Have!'))
        if guess < target:
            print('Too Few!')
            continue
        elif guess > target:
            print('Too Many!')
            continue
        else:
            print('You\'re Right!')
            return
            run_apple_guessing_game(5)



while True:
    username = input('What is your username?')
    if username != 'admin':
        continue
    password = input('What is your password?')
    if password == 'topsecret':
        break
print('Authorised')


list = ['fourteen', 'fifteen', 16, 'seventeen']
for item in list:
    try:
        msg = 'processing ' + item
        print(msg)
        continue
    except TypeError:
        print('something went wrong!')
        break
    finally:
        print('finally block')
    print('next item please!')


#
# def format_string(msg, prefix = 'String: ', postfix) -> int:
#     print(prefix + msg + postfix)
#
# format_string('hello', postfix='.')
