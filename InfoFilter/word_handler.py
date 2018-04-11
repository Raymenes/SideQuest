import re
import string
import operator


def get_word_list(words):
    words = words.lower()
    word_list = words.split()
    invalid_chars = set(string.punctuation.replace("_", ""))

    for i in range(2):
        for word in word_list:
            if any(char in invalid_chars for char in word):
                clean_word = re.sub('[^A-Za-z0-9]+', '', word)
                word_list.remove(word)
                word_list.append(clean_word)
    return word_list


def get_word_set(words):
    return set(get_word_list(words))


def get_word_frequency_list(words):
    word_list = get_word_list(words)
    word_map = {key:0 for key in set(word_list)}
    for word in word_list:
        word_map[word] += 1
    return sorted(word_map.items(), key=operator.itemgetter(1), reverse=True)
