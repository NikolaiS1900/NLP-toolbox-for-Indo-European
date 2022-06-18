TEXT = "bonde bondæ bondens bon katte"

WORD_LIST = TEXT.split()


# This function is written by Sonia Pickering
# It was originally a part of an experiment to convert Enlgish words to Latin.
# However, it does not need to be used with Latin.
def convert_to_latin(word):
    word = word.replace("bo", "ba")
    #word = word.replace("", "")
    #word = word.replace("", "")
    #word = word.replace("", "")
    #word = word.replace("", "")
    #word = word.replace("", "")
    #word = word.replace("", "")
    #word = word.replace("", "")
    #word = word.replace("", "")
    #word = word.replace("", "")
    #word = word.replace("", "")
    return word


RESULT = [convert_to_latin(word) for word in WORD_LIST]
print(RESULT)
