from string import ascii_lowercase


def get_num_attempts():
    while True:
        num_attempts = input(
            'How many incorrect attempts do you want? [1-10] ')
        try:
            num_attempts = int(num_attempts)
            if 1 <= num_attempts <= 25:
                return num_attempts
            else:
                print('{0} is not between 1 and 10'.format(num_attempts))
        except ValueError:
            print('{0} is not an integer between 1 and 10'.format(
                num_attempts))


def get_min_word_length():
    while True:
        min_word_length = input(
            'What minimum word length do you want? [4-8] ')
        try:
            min_word_length = int(min_word_length)
            if 4 <= min_word_length <= 16:
                return min_word_length
            else:
                print('{0} is not between 4 and 8'.format(min_word_length))
        except ValueError:
            print('{0} is not an integer between 4 and 8'.format(min_word_length))
