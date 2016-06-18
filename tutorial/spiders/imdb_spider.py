import scrapy
from tutorial.items import EpisodeItem

class ImdbSpider(scrapy.Spider):
		name = "imdb"
		allowed_domains = ["imdb.com"]
		start_urls = [
				"http://www.imdb.com/title/tt0060028/episodes?ref_=tt_ov_epl",
				"http://www.imdb.com/title/tt0060028/episodes?season=2",
				"http://www.imdb.com/title/tt0060028/episodes?season=3"
		]

		def parse(self, response):
				for episodeDiv in response.xpath("//div[@class='list detail eplist']/div"):
					infoDiv = episodeDiv.xpath("div[@class='info']")
					imageDiv = episodeDiv.xpath("div[@class='image']")
					episode = EpisodeItem()
					episode["index"] = imageDiv.xpath("a/div/div/text()").extract()
					episode["link"] = infoDiv.xpath("strong/a/@href").extract()
					episode["title"] = infoDiv.xpath("strong/a/@title").extract()
					episode["description"] = infoDiv.xpath("div[@class='item_description']/text()").extract()
					yield episode


							
