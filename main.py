from stats import count_words
from stats import count_chars
from stats import chars_sort
import sys

if len(sys.argv) != 2:
     print('Usage: python3 main.py <path_to_book>')
     sys.exit(1)

def get_book_text():
        with open(f'{sys.argv[1]}') as t:
            book_text = t.read()
        return book_text

def main():
    out_text = get_book_text()
    word_count = count_words(out_text)
    char_count = count_chars(out_text)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {sys.argv[1]}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    chars_sort(char_count) 
    print('============= END ===============')

main()