#!/usr/bin/env python

from random import randint
from random import choice

def markov(filename, word_count):
    word_dict = {}
    word_tuple = []
    
    with open(filename, "r") as file:
        story = file.read()

    words = story.split()
    word_length = len(words)
    counter = 0

    while word_length > 1:
        word_tuple.append((words[counter], words[counter+1]))
        word_length -= 1
        counter += 1

    for tup in word_tuple:
        key = tup[0].lower()
        value = tup[1]
        
        if key in word_dict:
            word_dict[key].append(value)
        else:
            word_dict[key] = [value]

    markov = []
    first_index = randint(0, len(words)-2)
    first_word = words[first_index]
    second_word = words[first_index+1]
    markov.append(first_word)
    markov.append(second_word)

    counter_too = 2
    while counter_too < word_count:
        if second_word == words[len(words)-1]:
            first_word = words[first_index]
        else:
            first_word  = second_word
        second_word = choice(word_dict[first_word]).lower()
        markov.append(second_word)
        counter_too += 1
  
    return ' '.join(markov)
