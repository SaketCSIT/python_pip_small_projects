import langid

def lang(text):
    return langid.classify(text)[0]

text=input('Enter Any Language\n')
print(lang(text))