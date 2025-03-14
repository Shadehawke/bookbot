import sys
from stats import word_count
from stats import character_count
from stats import sort_list

if len(sys.argv) > 1:
    for arg in sys.argv:
        filepath = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
     
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(filepath)
    num_words = word_count(text)
    char_count = character_count(text)
    sorted_list = sort_list(char_count)
    
    
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at ...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
    

    



main()