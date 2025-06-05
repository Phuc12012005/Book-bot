
def get_num_words(file_contents):
    num_words = len(file_contents.split())
    return num_words

def count_char(file_contents):
    word_count = {}
    for char in file_contents.lower():
        if char in word_count:
            word_count[char] += 1
        else:
            word_count[char] = 1
    return word_count

def sort_on(unsorted_word_count):
    return unsorted_word_count["num"]

def sort_word_count(word_count):
    sort_list = []
    for key, value in word_count.items():
        sort_list.append({"char": key, "num": value})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list



