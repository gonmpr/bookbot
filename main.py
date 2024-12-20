### BookBot ###
"""
Takes a book as an input, escifically the path to the book, and returns:

- number of words in the book
- amount of times the letters appears

"""

book_path = "books/frankenstein.txt"




def main():

    text = get_book_text(book_path)

    word_occurrences = list_letters(count_letters(text))
    word_occurrences.sort(reverse=True, key=sort_on)

    #this function is especifically made for the method sort(), this way it sorts in base of the number of times the letter appears
    def sort_on(dict):
        return dict["times"]


    print(f"--- Begin report of {book_path} ---\n")
    print(f"{count_words(text)} words found in the document\n")
    
    for word in word_occurrences:
        if word["letter"].isalpha():
            print(f"The {word["letter"]} character was found {word["times"]} times")
    print("\n--- End report ---")












#get the text out of the book and make it usable by python, the parameter is the path of the book
def get_book_text(book):


        with open(book) as f:
            return f.read()



#count the amount of ocurrences of each word that is on the book
def count_words(text):
    words = text.split()
    
    return len(words)




#count the amount of ocurrences of each letter that is on the book
def count_letters(text):
    text_lower = text.lower()
    letters = dict()

    for char in text_lower:

        if letters.get(char) is not None:
            letters[char] = letters.get(char) + 1
        else:
            letters[char] = 1
    return letters




#transform the dictionary from {letter: times, letter: times, etc...} to ({letter: times}, {letter: times}, etc...)
def list_letters(letters_dict_format):
    letter_list_format = list()
    for key,value in letters_dict_format.items():
          letter_list_format.append({"letter": key, "times": value})
        
    return letter_list_format



main()