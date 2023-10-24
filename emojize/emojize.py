import emoji
Input = input("Input: ")
if '_' in Input:
    print(emoji.emojize(Input))
else:
    print(emoji.emojize(Input,language='alias'))