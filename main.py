# import libraries
import string

# create a hash table to store words in the dictionary
dictionary = {}

# read in the large dictionary file and add words to the hash table
with open("large_dictionary.txt", "r") as f:
    for line in f:
        # remove any leading or trailing whitespace
        word = line.strip()
        # convert word to lowercase
        word = word.lower()
        # add word to the hash table
        dictionary[word] = True

# read in the personal dictionary file and add words to the hash table
with open("personal_dictionary.txt", "r") as f:
    for line in f:
        # remove any leading or trailing whitespace
        word = line.strip()
        # convert word to lowercase
        word = word.lower()
        # add word to the hash table
        dictionary[word] = True

# function to find misspelled words in a text file
def spell_check(filename):
    # open the text file
    with open(filename, "r") as f:
        # initialize line number counter
        line_num = 0
        # loop through each line in the file
        for line in f:
            # increment line number counter
            line_num += 1
            # remove punctuation from the line
            line = line.translate(str.maketrans("", "", string.punctuation))
            # split the line into individual words
            words = line.split()
            # loop through each word in the line
            for word in words:
                # convert word to lowercase
                word = word.lower()
                # check if the word is in the hash table
                if word not in dictionary:
                    # print the misspelled word and its line number
                    print(f"Misspelled word '{word}' found on line {line_num}")
                    # create a list to store suggested words
                    suggested_words = []
                    # check if any words can be formed by adding one character
                    for i in range(len(word)+1):
                        for letter in string.ascii_lowercase:
                            new_word = word[:i] + letter + word[i:]
                            if new_word in dictionary:
                                suggested_words.append(new_word)
                    # check if any words can be formed by removing one character
                    for i in range(len(word)):
                        new_word = word[:i] + word[i+1:]
                        if new_word in dictionary:
                            suggested_words.append(new_word)
                    # check if any words can be formed by exchanging adjacent characters
                    for i in range(len(word)-1):
                        new_word = word[:i] + word[i+1] + word[i] + word[i+2:]
                        if new_word in dictionary:
                            suggested_words.append(new_word)
                    # print the suggested words
                    print(f"Suggested words: {', '.join(suggested_words)}")

# example usage of the spell_check function
spell_check("sample_text.txt")
