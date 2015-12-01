from scoop import futures
import re
import sys


def count_words(filename):
    """Count the number of times every word in the file `filename`
       is contained in this file. Return the result as a dictionary,
       where the key is word, and the value is the number of times
       the word appears in the file"""
    lines = open(filename, "r").readlines()

    all_words = {}

    for line in lines:
        words = line.split(" ")

        for word in words:
            #lowercase the word and remove all
            #characters that are not [a-z] or hyphen
            word = word.lower()
            match = re.search(r"([a-z\-]+)", word)

            if match:
                word = match.groups()[0]
                
                if word in all_words:
                    all_words[word] += 1
                else:
                    all_words[word] = 1

    return all_words


def reduce_dicts( dict1, dict2 ):
    """Combine (reduce) the passed two dictionaries to return
       a dictionary that contains the keys of both, where the
       values are equal to the sum of values for each key"""

    # explicitly copy the dictionary, as otherwise
    # we risk modifying 'dict1'
    combined = {}

    for key in dict1.keys():
        combined[key] = dict1[key]

    for key in dict2.keys():
        if key in combined:
            combined[key] += dict2[key]
        else:
            combined[key] = dict2[key]

    return combined


if __name__ == "__main__":
    # need to call it using python countwords.py ../shakespeare/*
    files = sys.argv[1:]

    total_dict = futures.mapReduce(count_words, reduce_dicts, files)
    words = sorted([k for k, v in total_dict.iteritems() if v > 2000])

    def print_line(word, count):
        print word, ' = ', count

    map(print_line, words, [total_dict[x] for x in words])

    # use Counter here?