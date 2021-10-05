#code for word count

paragraph= """
Growing up, they remember a home filled with state-of-the-art technology — like an early digital clock and some of the first home computers.
They came to StoryCorps to reflect on their unforgettable childhood and their father’s colossal personality.
"""

"""
1) How many words in the paragraph : example count of the words
2) How many unique words: 
3) How many characters:
4) Need count of characters
5) I need count of special characters
6) Print all the special characters
"""

all_words = paragraph.split()
print(f"1) Number of words: {len(all_words)}")
print(f"2) Number of unique words: {len(set(all_words))}")
print(f"3) Number of characters: {len(paragraph)}")
print(f"4) Number of unique characters: {len(set(paragraph))}")
special_char_defined = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~—’"
special_char_included = set(special_char_defined).intersection(set(paragraph))
print(f"5) Number of special characters: {len(special_char_included)}")
print("6) Special characters: " + " ".join(special_char_included))