import scrapy

class MovieSubsSpider(scrapy.Spider):
    name = 'transcripts'
    allowed_domains = ['subslikescript.com']
    start_urls = ['https://subslikescript.com/movies']

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    def parse(self, response):
        movies = response.xpath('//ul[@class="scripts-list"]/a')
        
        for movie in movies:
            title = movie.xpath('li/text()').get()
            movie_url = movie.xpath('@href').get()
            
            if movie_url:
                movie_page = response.urljoin(movie_url)
                yield scrapy.Request(url=movie_page, callback=self.parse_movie_data, meta={'title': title, 'url': movie_url })

        next_page = response.xpath('(//a[@rel="next"]/@href)[2]').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_movie_data(self, response):
        title = response.request.meta['title']
        url = response.request.meta['url']
        plot = response.xpath('//p[@class="plot"]/text()').get()
        script = response.xpath('//div[@class="full-script"]/text()').getall()
        script = ' '.join(script)

        yield {
            'title': title,
            'url': url,
            'plot': plot,
            'script': script,
        }