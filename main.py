import sys
from stats import *

def main():
   if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)

   book_path = sys.argv[1] 
   book_text = get_book_text(book_path)
   chars = sorted_chars(count_chars(book_text))

   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {book_path}...")
   print("----------- Word Count ----------")
   print(count_words(book_text))
   print("--------- Character Count -------")
   for letter in chars:
      if not letter["name"].isalpha():
         continue
      print(f"{letter['name']}: {letter['num']}")
   print("============= END ===============")

main()
