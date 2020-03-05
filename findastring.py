# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
#  String traversal will take place from left to right, not from right to left.


def count_substring(string, sub_string):
    start = 0
    counter = 0
    end = len(sub_string)
    while(True):
        if (string[start:end] == (sub_string)):
            counter += 1
        start += 1
        end += 1
        if(start >= len(string)):
            break;
    return counter
