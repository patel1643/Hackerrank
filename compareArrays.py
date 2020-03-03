# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.
#
# For example, given input  and , we find  instances of ',  of '' and  of ''. For each query, we add an element to our return array, .
#
# Function Description
#
# Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.
#
# matchingStrings has the following parameters:
#
# strings - an array of strings to search
# queries - an array of query strings
# Input Format
#
# The first line contains and integer , the size of .
# Each of the next  lines contains a string .
# The next line contains , the size of .
# Each of the next  lines contains a string .
#
# Output Format
#
# Return an integer array of the results of all queries in order.




def matchingStrings(strings, queries):
    finalScores = []
    counter = 0
    for i in range(len(queries)):
        for j in range(len(strings)):
            if(queries[i] == strings[j]):
                counter += 1
        finalScores.append(counter)
        counter = 0

    return finalScores
