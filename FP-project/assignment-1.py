# Advanced Python Programming - FP Project | Author: Javier Pardos | javier.pardos10@e-uvt.ro

"""
Assigment 1 - Write a program that reads a text file, decodes it with the given replacements
and prints on the screen all the words starting with 'a'.

All these operations will be implemented using the functional programming style
"""

from typing import List

def replace_char(char :chr) -> chr:

    """ Pure function - Replaces a character with another one """

    replacements = {'!':'s', '@':'h', '#':'e', '$':'r', '%':'l', '^':'o', '&':'c', '*':'k'}

    # return the replacement key if exists in dict, else return the same char that was given 
    # becasuse it means that it is not a special character
    return replacements.get(char, char)


def decode_text(text: str) -> str:

    """ Decodes the text with the given replacements """

    # 'join()' doesnt modifies the original string, it returns a new one
    # 'map()'  is given an iterable collection, and a function that it will apply to each element 
    #          in this case the string its the original text and 'replace_char()' is the function 
    #          that will be applied to each char

    return ''.join( map(replace_char, text) )


def find_words(text: str, letter: str) -> List[str]:

    """ Finds all the words starting with the given letter """
    
    # split the text by spaces, into a list of words
    splitted_text = text.split()

    # 'filter()'  is given an iterable collection, splitted_text (words from text)
    #             and a function that will be applied to each element, 'startswith(letter)'
    #
    # lambda function is used to iterate over the list of words and check 
    #                 if the word starts with the given letter, as an anonymous function
    #
    # return a list with the result of the filter function
    return list( filter(lambda word: word.startswith(letter), splitted_text) )

def main():

    # read the file sherlock.txt
    with open('sherlock.txt', 'r') as file:
        text = file.read()

    ##print(text)

    # apply the decode function to the text
    decoded_text = decode_text(text)

    ##print(decoded_text)

    # find words starting with 'a' 
    words = find_words(decoded_text, 'a')

    # print the words
    print(words)

if __name__ == '__main__':
    main()
