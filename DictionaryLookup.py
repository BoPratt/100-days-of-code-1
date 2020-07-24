from PyDictionary import PyDictionary as p

word = input('What word would you like to know? ')
try:
    wType = p.meaning(word, disable_errors=IndexError)
    meaning = wType.get(list(wType)[0])
    print(f'{list(wType)[0]};\n\nMeaning(s): {". OR ".join(meaning)}.')
except AttributeError:
    print('You fool, that\'s not a word')


