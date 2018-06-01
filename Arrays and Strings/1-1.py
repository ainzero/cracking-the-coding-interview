

def isUnique(string):

    # Assuming extended ASCI with a alphabet size of 256
    alphabet_size = 256

    # a string larger than the alphabet size must contain duplicates
    if (len(string) > alphabet_size):
        return False

    # create an array of boolean values that is the size of the alphabet
    alphabet = [False]*alphabet_size

    for letter in string:
        ascii_code = ord(letter)

        letter_has_been_seen = alphabet[ascii_code]

        if letter_has_been_seen:
            # return false if a duplicate letter is seen
            return False
        else:
            #
            alphabet[ascii_code] = True

    # no duplicate letters have been seen, the string has all unique characters
    return True


def isUniqueNoDS(string):

    # Assuming extended ASCI with a alphabet size of 256
    alphabet_size = 256

    # a string larger than the alphabet size must contain duplicates
    if (len(string) > alphabet_size):
        return False

    # The brute force approach would run in O(N^2) time.
    for test_letter_index in range(len(string)):
        for comparison_letter_index in range(len(string)):
            # skip this index since we would be comparing a letter to itself
            if test_letter_index == comparison_letter_index:
                continue
            # if the letter is the same, then its a duplicate and return false
            if string[test_letter_index] == string[comparison_letter_index]:
                return False

    # if the function gets here, then all letters in the string are unique
    return True


def main():
    test_string = "abcdea"
    another_test_string = "abcdef"

    print("isUnique: " + test_string +
          " : " + str(isUnique(test_string)))
    print("isUnique: " + another_test_string +
          " : " + str(isUnique(another_test_string)))

    print("isUniqueNoDS: " + test_string +
          " : " + str(isUniqueNoDS(test_string)))
    print("isUniqueNoDS: " + another_test_string +
          " : " + str(isUniqueNoDS(another_test_string)))


if __name__ == '__main__':
    main()
