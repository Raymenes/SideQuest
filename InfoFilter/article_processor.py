import word_handler as word
import article
import json
import re
import datetime
from yattag import Doc



def load_json_data(file_path):
    return json.load(open(file_path, 'r'))


path = "/Personal/DeepLearning/SideQuest/scapper/itemsTechCrunch.json"
out_folder_path = "/Personal/DeepLearning/SideQuest/Article_Data/"

json_data = load_json_data(path)
article_list = []
words = ''

for item in json_data:
    content = item.get('text')
    content = re.sub('\.', '. ', content)
    content = re.sub('[ ]{2,}', ' ', content)
    item['text'] = content

########
date_str = datetime.date.today().strftime("%Y-%m-%d")
filename = "techcrunch" + "_" + date_str
with open(out_folder_path+filename+".json", 'w+') as outfile:
    json.dump(json_data, outfile, indent=4)
########

########
for item in json_data:
    doc, tag, text = Doc().tagtext()
    title = item.get('title')[0]
    with tag('html'):
        with tag('header'):
            with tag('h1'):
                text(title)
        with tag('body'):
            with tag('p', id='content'):
                text(item.get('text'))
            with tag('p', id='date'):
                text(item.get('date'))
            with tag('a', href=item.get('url')):
                text('view tech crunch web page')
    file_title = re.sub('[^\w+$]|/', '_', title).replace(' ', '_')
    with open(out_folder_path + file_title + ".html", 'w+') as html_file:
        html_file.write(doc.getvalue())
        html_file.close()
########

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
