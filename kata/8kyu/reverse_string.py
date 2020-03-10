# reverse a string
import string


def reverseWords(input_string):
    input_words = input_string.split(" ")
    input_words = input_words[-1::-1]

    output = ' '.join(input_words)

    return output


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
print(removePunctuationAndReverseWords("test one!"))  # one test
print(removePunctuationAndReverseWords("this!! is!! !a! test?!@"))  # test a is this
