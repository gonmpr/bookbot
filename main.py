from stats import *
def main():
   book_path = 'books/frankenstein.txt' 
   book_text = get_book_text(book_path)
   print(count_words(book_text))
   print(count_chars(book_text)) 


main()
