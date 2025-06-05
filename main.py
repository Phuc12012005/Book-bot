from stats import get_num_words

# A with block can be used to open a file:
# The with block will automatically close the file when the block is exited, cleaning up resources.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents



def main():
    file_contents = get_book_text("books/frankenstein.txt")
    get_num_words(file_contents)

main()