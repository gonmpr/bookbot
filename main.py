
book_path = "books/frankenstein.txt"

def main():

    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---\n")
    print(f"{count_words(text)} words found in the document\n")
    
    
    def sort_on(dict):
        return dict["times"]
    
    word_occurrences = list_letters(count_letters(text))
    word_occurrences.sort(reverse=True, key=sort_on)

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


def list_letters(dictionary):
    list_letters = list()
    for key,value in dictionary.items():
          list_letters.append({"letter": key, "times": value})
        
    return list_letters



main()