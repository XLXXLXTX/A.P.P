# Advanced Python Programming - FP Project | Author: Javier Pardos | javier.pardos10@e-uvt.ro

"""
Assigment 2 - Make a program that will do the following:

a) read a word from the input console
b) Creates all anagrams of that word
c) Compare all anagrams created at the previous step with the words contained in the
file dictionary.txt, attached to this laboratory (see on the classrooms materials). If the
word exists in that dictionary, it means that the word is meaningful and display it.

"""

from itertools import permutations

def create_anagrams(word: str) -> list:

    """ Creates all anagrams of the given word """

    # 'permutations()' returns a list of tuples with all the permutations of the given word
    # 'join()'         joins the tuples into a string
    #
    # return a list created from a list comprehension
    return [ ''.join(p) for p in permutations(word) ]

def compare_anagrams(anagrams: list, dict_path: str) -> list:
    
    """ Load and check all anagrams with the words from the dictionary """

    # initialize the empty set for the words from the dictionary
    dictionary = {}

    # read the dictionary file and split it into a list of words adding to the set
    with open(dict_path, 'r') as file:
        dictionary = file.read().split()
    
    # 'filter()'  is given an iterable collection, anagrams (list of anagrams)
    #             and a lambda function that will be applied to each element 
    #             checking if the word is in the dictionary
    #
    # return a list with the result of the filter function
    return list( filter(lambda word: word in dictionary, anagrams) )


def main():

    # ask user for a word
    word = input("Enter a word: ")

    # create a list with all the posible anagrams of the given word
    anagrams = create_anagrams(word)

    #print(anagrams)

    # compare all anagrams with the words from the dictionary
    meaningful_words = compare_anagrams(anagrams, 'dictionary.txt')

    # print the meaningful words
    print(meaningful_words)


if __name__ == '__main__':
    main()