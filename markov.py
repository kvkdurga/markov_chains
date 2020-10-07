"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path).read()
    

    return file

#string = (open_and_read_file("green-eggs.txt")

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    # next_word = []
    words = text_string.split()
    words.append(None)

    for i in range(len(words) - 2):
        # chains = (words[i],words[i+1]),[words[i+2]])
        key_words = (words[i],words[i+1])
        value_words = words[i+2]
        #chains[key_words] = value_words

        if key_words not in chains:
            chains[key_words] = []
            
        chains[key_words].append(value_words)
            
        # chains = (words[i],words[i+1])

        #animals['pony'] = 2
        #for key_words in words.items():
        

        #chains[next_word] = chains.get((words[i], words[i + 1], words[i+2]) 
        #next_word)next_word.append(words[i + 2]))


        #next_word.append(words[i + 2])
    #letter_counts[letter]=letter_counts.get(letter, 0)+1
    #your code goes here
    #print('{} and {}\n'.format(key_words, value_words))
    return chains

#words = open_and_read_file("green-eggs.txt")
#print(make_chains(words))

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    dict_key = choice(list(chains.keys()))
    #print(dict_key)
    words = [dict_key[0], dict_key[1]]
    #print(words)
    word = choice(chains[dict_key])
    #print(word)
    while word is not None:
        dict_key = (dict_key[1], word)
        words.append(word)
        word = choice(chains[dict_key])

    return ' '.join(words)


input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
