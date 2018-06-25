def isPermutationOfPalindrone(str):
    # remove spaces
    str = str.replace(" ","")
    str_length = len(str)

    is_even_length = str_length % 2 == 0

    list_string = list(str)
    
    char_dict = {}
    for char in list_string:    
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    '''
    Palindrones with even length have an even number of characters while
    palindrones with odd lengths have a single 'pivot' character in addition
    to characters with even counts
    '''
    
    one_pivot_char = False
    for v in char_dict.values():
        if not is_even_length and v == 1 and not one_pivot_char:
            one_pivot_char = True
            continue

        even_number_of_chars = v % 2 == 0

        if not even_number_of_chars or (one_pivot_char and v == 1):
            return False # an odd number of characters indicates the word isn't a palindrone
    

    return True
            

def main():
    test_string_odd = "baby bab"
    test_string_even = "avid diva"
    test_string_even2 = "vida aivd"

    not_palindrone = "food bood"
    
    print(isPermutationOfPalindrone(test_string_odd))
    print(isPermutationOfPalindrone(test_string_even))
    print(isPermutationOfPalindrone(test_string_even2))
    print(isPermutationOfPalindrone(not_palindrone))


if __name__ == '__main__':
    main()