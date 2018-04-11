import word_handler as word
import article
import json
import re


def load_json_file(file_path):
    return json.load(open(file_path, 'r'))


path = "/Personal/DeepLearning/SideQuest/scapper/itemsTechCrunch.json"

json_file = load_json_file(path)
article_list = []
words = ''

for item in json_file:
    content = item.get('text')
    content = re.sub('\.', '. ', content)
    content = re.sub('[ ]{2,}', ' ', content)
    print(content)

# word_set = word.get_word_set(words)
# for i in word_set:
#     print(i)

# word_frequency_map = word.get_word_frequency_list(words)
# print("word_frequency_map size = "+str(len(word_frequency_map)))
#
# for i in word_frequency_map:
#     print(i)

# filename = "should-ai-researchers-kill-people"
#
# article = open(path+filename, 'r').read()
# wordList = word.get_word_list(article)
# wordSet = set(wordList)
# word_frequency_map = word.get_word_frequency_list(article)
#
#
# print("wordList size = " + str(len(wordList)))
# print("wordSet size = "+str(len(wordSet)))
# print("word_frequency_map size = "+str(len(word_frequency_map)))
# print(word_frequency_map)
#
