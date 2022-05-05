import pyperclip


def transform(text, key, task):
    result = ''
    if task == 'd':
        key *= -1
    for letter in text:
        result += chr(ord(letter) + key)
    return result


def main():
    print('Caesar cyper')
    while True:
        task = input("What do you want? (e)ncript, (d)ecript or (ex)it?:\n")
        if task == 'ex':
            break
        while True:
            key = int(input('Enter the key. (between 0 and 30):\n'))
            if key in range(0, 31):
                break
        text = input('Enter the message:\n')
        result = transform(text, key, task)
        pyperclip.copy(result)
        print(result)
        print('Text is copied to clipboard.')
        print()


if __name__ == '__main__':
    main()
