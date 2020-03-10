# reverse a string
import string


def reverseWords(input_string):
    input_words = input_string.split(" ")
    input_words = input_words[-1::-1]

    output = ' '.join(input_words)

    return output


def removePunctuationAndReverseWords(input_string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for x in input_string.lower():
        if x in punctuations:
            input_string = input_string.replace(x, "")

    input_words = input_string.split(" ")
    input_words = input_words[-1::-1]
    output = ' '.join(input_words)

    return output


print(reverseWords("test output"))  # output test
print(reverseWords("hi, my name is steve!"))  # steve! is name my hi,
print(removePunctuationAndReverseWords("test one!"))  # one test
print(removePunctuationAndReverseWords("this!! is!! !a! test?!@"))  # test a is this
