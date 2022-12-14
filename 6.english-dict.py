import json
from difflib import get_close_matches

data = json.load(open("./data/data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) >0:
        yn = input("Did you mean %s instead?\nEnter Y if Yes, or N if No: " % get_close_matches(word,data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exist. Please double check it!!"
        else:
            return "We didn't Understand your Entry"
    else:
        return "The word doesn't exist. Please double check it!!"


word = input("Enter the Word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
