###more advanced attempt at useing scrapy to scrape and parse webdata and then 
###save it too a .csv

import scrapy
import csv

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2018']
    f = csv.writer(open('2018_brickset_info.csv', 'w'))
    f.writerow(['Name','Pieces','Minifigs','Image'])

    def parse(self, response):
        SET_SELECTOR = '.set'
        
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h1 a ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            #PRICE_SELECTOR = './/dl[dt/text() = "RRP"]dd/text()'
            IMAGE_SELECTOR =  'img ::attr(src)'
          
            name = brickset.css(NAME_SELECTOR).extract(),
            pieces = brickset.xpath(PIECES_SELECTOR).extract_first(),
            minifigs = brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
            #price = brickset.xpath(PRICE_SELECTOR).extract_first(),
            image = brickset.css(IMAGE_SELECTOR).extract_first()
            	
            print(name)
            print(pieces)
            print(minifigs)
            #print(price)
            print(image)
            f.writerow([name, pieces, minifigs, image])

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
        	yield scrapy.Request(
        		response.urljoin(next_page),
        		callback=self.parse
        	)