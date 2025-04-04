from stats import book_text_to_string
from stats import counts_char_symb_space
from stats import sorted_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    print("sys.argv:", sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
   
    text = get_book_text(path_to_file)
   
    word_count = book_text_to_string(text)  # Make sure you have this function

    char_counts = counts_char_symb_space(text)
    char_list = sorted_list(char_counts)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character count (only for alphabetical characters)
    for item in char_list:
        char = item["character"]
        count = item["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    
    print("============= END ===============")
    

if __name__== "__main__":
    main()