from stats import *
import sys


# A with block can be used to open a file:
# The with block will automatically close the file when the block is exited, cleaning up resources.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 main.py <path_to_book>")
    print("============ BOOKBOT ============")
    path_to_file = sys.argv[1]
    print(f"Analyzing book found at {path_to_file}")

    print("----------- Word Count ----------")
    file_contents = get_book_text(path_to_file)
    num_words = get_num_words(file_contents)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    word_count = count_char(file_contents)
    
    word_count_list = sort_word_count(word_count)
    for pair in word_count_list:
        if pair["char"].isalpha() == False:
            continue
        print(pair["char"] + ":",pair["num"])

    print("============= END ===============")


main()