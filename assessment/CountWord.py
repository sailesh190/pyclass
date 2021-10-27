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
import re

print("1) Number of words:",len(paragraph.split()))
print("2) Number of unique words:",len(set(paragraph.split())))
print("3) Number of characters:",len(paragraph))

dict = {}
for c in sorted(set(paragraph)):
      k = paragraph.count(c)
      dict[c] = k
print("4) Count of characters:",dict)

specialChar=[]
specialChar = set(re.findall(r'[^a-zA-Z0-9{}\n]',paragraph))
dict1 = {}
for c1 in set(specialChar):
    k1 = paragraph.count(c1)
    dict1[c1] = k1
print("5) Count of special characters:",dict1)
print("6) All of the special characters:",specialChar)
