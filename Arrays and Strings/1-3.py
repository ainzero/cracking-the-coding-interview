
def formatString(str, true_str_len):
    string_as_list = list(str)
    
    # counts how many times we examine an element
    # of the 'true string'
    counter = 0
    
    # used to keep the mapping between the original string and
    # the list of characters we modify accurate
    removed = 0
    
    in_string = False
    for index in range(len(str)):

        if in_string:
            if str[index] == ' ':
                string_as_list[index - removed]= "%20"
            counter += 1
        else:
            if str[index] == ' ':
                del string_as_list[index - removed]
                removed += 1
            else:
                in_string = True
                counter += 1
                
        if counter == true_str_len:
            break
    
    return "".join(string_as_list)


def main():
    test_string = "  Mr.John Smith       "    
    true_string_length = 13

    print(formatString(test_string,true_string_length))

if __name__ == '__main__':
    main()