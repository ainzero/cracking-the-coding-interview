

def isPermutation(str_a, str_b):

    # Assuming an ASCII alphabet

    # str_b and str_a must have the same length, or they are not permutations
    if len(str_a) != len(str_b):
        return False

    # the strings are permutations if they are identical when sorted
    return sorted(str_a) == sorted(str_b)


def main():
    # some test strings
    some_str = "Anthony"
    another_str = "Tony"
    last_str = "noyT"

    print(isPermutation(some_str, last_str))
    print(isPermutation(last_str, another_str))


if __name__ == '__main__':
    main()
