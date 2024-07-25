def translate(inText):
    outputstr=""
    for index in inText:
        if index.lower() in "aeiou":
            if index.isupper():
                outputstr = outputstr + "G" 
            elif index.islower():
                outputstr = outputstr + "g"
        else:
            outputstr = outputstr + index
    return outputstr

print("Welcome to the Giraffe Translator!")
inText = input("Please enter the phrase to be translated: ")
translatedtext = translate(inText)
print(f"You have entered {inText}. The translation for that is {translatedtext}")