# import emoji
# Input = input("Input: ")
# print(emoji.emojize(Input,language = 'en' or 'alias'))
import emoji


def main():
    emojize()


def emojize():
    user_input = input("Input: ")
    print(emoji.emojize(user_input))


if __name__ == "__main__":
    main()