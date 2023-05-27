def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translate_sentence = ""
    generator_of_words = (word for word in sentence.split())
    for generator_word in generator_of_words:
        if (words.get(generator_word) != None):
            translate_sentence += words.get(generator_word)
            translate_sentence += " "
        else:
            return False
    return translate_sentence

def main():
    sentence = translate("el gato esta en la casa")
    if (sentence != False):
        print(sentence)
    else:
        print("cannot translate")


if __name__ == '__main__':
    main()