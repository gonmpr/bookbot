
def get_book_text(path):
   book_text = str()
   with open(path) as book:
      book_text = book.read() 

   return book_text

def count_words(text):
   words = text.split()
   return f"Found {len(words)} total words"

def count_chars(text):
   chars = dict()
   for char in text.lower():
      if char in chars:
        chars[char] += 1 
      else:
        chars[char] = 1
   return chars
   
