# reverse a string


def reverseWords(input):
    inputWords = input.split(" ")
    inputWords = inputWords[-1::-1]

    output = ' '.join(inputWords)

    return output


print(reverseWords("test output"))  # output test
print(reverseWords("hi, my name is steve!"))  # output test
