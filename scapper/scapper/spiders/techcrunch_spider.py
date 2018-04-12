from datetime import datetime, timedelta
import scrapy
#https://monkeylearn.com/blog/filtering-startup-news-machine-learning/#scraping-from-tech-news-sites
#to run this use scrapy crawl techcrunch -o filename.json

class TechCrunchSpider(scrapy.Spider):

    name = "techcrunch"

    def start_requests(self):
        start_date = datetime(2017, 1, 1)
        end_date = datetime(2017, 12, 31)

        date = start_date
        while date <= end_date:
            new_request = scrapy.Request(self.generate_url(date))
            new_request.meta["date"] = date
            new_request.meta["page_number"] = 1
            yield new_request
            date += timedelta(days=1)


    def generate_url(self, date, page_number=None):
        url = 'https://techcrunch.com/' + date.strftime("%Y/%m/%d") + "/"
        if page_number:
            url  += "page/" + str(page_number) + "/"
        return url


    def parse(self, response):
        date = response.meta['date']
        page_number = response.meta['page_number']

        # when I access a page number that doesn't exist I get 404
        # I could use the pagination buttons, but this is less work
        if response.status == 200:
            articles = response.xpath('//h2[@class="post-block__title"]/a/@href').extract()
            for url in articles:
                request = scrapy.Request(url,
                                callback=self.parse_article)
                request.meta['date'] = date
                yield request

            url = self.generate_url(date, page_number+1)
            request = scrapy.Request(url,
                            callback=self.parse)
            request.meta['date'] = date
            request.meta['page_number'] = page_number
            yield request



    def parse_article(self, response):

        yield {
            'title': response.xpath('//h1/text()').extract(),
            'text': response.xpath('//div[starts-with(@class,"article-content")]/p//text()').extract(),
            #'tags': response.xpath('//div[@class="loaded acc-handle"]/a/text()').extract(),
            'date': response.meta['date'].strftime("%Y/%m/%d"),
            'url' : response.url
        }