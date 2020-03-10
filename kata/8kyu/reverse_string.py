# reverse a string
import string


def reverseWords(input_string):
    input_words = input_string.split(" ")
    input_words = input_words[-1::-1]

    output = ' '.join(input_words)

    return output


def removePunctuation(input_string):
    for i in input_string.lower():
        if i in string.punctuation:
            input_string = input_string.replace(i, "")
    return input_string


def removePunctuationAndReverseWords(input_string):
    for i in input_string.lower():
        if i in string.punctuation:
            input_string = input_string.replace(i, "")

    input_words = input_string.split(" ")
    input_words = input_words[-1::-1]
    output = ' '.join(input_words)

    return output


print(reverseWords("test output"))  # output test
print(reverseWords("hi, my name is steve!"))  # steve! is name my hi,
print(removePunctuation("test one!"))  # test one
print(removePunctuation("this!! is!! !a! test?!@"))  # test a is this
print(removePunctuationAndReverseWords("test two!"))  # one test
print(removePunctuationAndReverseWords("this!! is!! !also! a- test?!@"))  # test a is this
