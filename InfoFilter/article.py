import json


class Article:
    title = ''
    author = ''
    url = ''
    tag = []
    date = ''
    content = ''

    def init_techcrunch_article(self, json_item):
        self.title = json_item.get('title')
        self.author = json_item.get('author')
        self.url = json_item.get('url')
        self.date = json_item.get('date')
        self.content = json_item.get('text')

