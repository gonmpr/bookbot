
def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(count_words(text))




def get_book_text(book):


        with open(book) as f:
            return f.read()




def count_words(text):
    words = text.split()
    
    return len(words)




main()