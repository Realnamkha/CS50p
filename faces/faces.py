def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text
def main():
    sentence = input("Enter your string ")
    sentence = convert(sentence)
    print(sentence)

main()