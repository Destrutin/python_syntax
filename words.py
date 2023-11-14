def print_upper_words(words, must_start_with):
    """ Print each word on a seperate line in uppercase."""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())