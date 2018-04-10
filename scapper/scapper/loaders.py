from idna import unicode
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


class TechCrunchArticleLoader(ItemLoader):
    default_input_processor = MapCompose(lambda s: unicode(s, "utf-8"), unicode.strip)
    default_output_processor = Join()

    title_in = MapCompose(unicode.strip, unicode.title)
    title_out = Join()

    text_in = MapCompose(unicode.strip)
    text_out = Join()

    tags_in = MapCompose(unicode.strip)
    tags_out = Join(separator=u'; ')

class RecodeArticleLoader(TechCrunchArticleLoader):
    subtitle_in = MapCompose(unicode.strip)
    subtitle_out = Join()

class VentureBeatArticleLoader(TechCrunchArticleLoader):
    pass
