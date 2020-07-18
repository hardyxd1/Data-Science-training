import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def traslate(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) >0:
        yn=input("Did you men %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0]).upper()
        if yn== "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exist. Please double check it."
        else:
             return "We didn't understand your entry"

    else:
        return "The word dosent exist. Prease double check Rait."

word= input("Enter word:  ").lower()

output= traslate(word)

if type(output) is list:

    for i in output:
        print(i)
else:
    print(output)