import scrapy

from tutorial.items import EpisodeItem


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["imdb.com"]
    # Season 1 page episode list of Star Trek the Orginal series
    start_urls = [
        "http://www.imdb.com/title/tt0060028/episodes",
        # "http://www.imdb.com/title/tt0060028/episodes?season=2",
        # "http://www.imdb.com/title/tt0060028/episodes?season=3"
    ]

    seasonIndex = 1

    # rule to follow "next season" type of links
    # rules = [
    # Rule(LxmlLinkExtractor(), callback=parse, follow=True)
    # ]

    # Parse season episode list to extract link for each episode
    def parse(self, response):
        # parse the list of episodes in the page
        for episodeDiv in response.xpath("//div[@class='list detail eplist']/div"):
            infoDiv = episodeDiv.xpath("div[@class='info']")
            imageDiv = episodeDiv.xpath("div[@class='image']")
            episode = EpisodeItem()
            episode["index"] = imageDiv.xpath("a/div/div/text()").extract()
            episode["link"] = infoDiv.xpath("strong/a/@href").extract()
            episode["title"] = infoDiv.xpath("strong/a/@title").extract()
            episode["description"] = infoDiv.xpath(
                "div[@class='item_description']/text()").extract()
            yield episode

        # The next page to follow will have ?episodes=n url param
        # todo: Find number of seasons from drop down at the top of the page
        nextUrl = reponse.request.url + "?season=" + (++seasonIndex)
        yield scrappy.Request(url=nextUrl, self.parse)
