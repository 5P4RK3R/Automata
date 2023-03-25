import scrapy


class MusicnotesSpider(scrapy.Spider):
    name = 'musicnotes'
    allowed_domains = ['https://www.musicnotes.com/']
    start_urls = ['https://www.musicnotes.com/']

    def parse(self, response):
        for musicnotes in response.css('div.newest-slider'):
            name = music_notes.css('a::text').get()
            try:
                if name =='\n                    ':
                    pass
                else:
                    yield  {
                        'name': name,
                        'link': music_notes.css('a').attrib['href']
                    }
            except:
                pass
