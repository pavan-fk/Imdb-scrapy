import scrapy

from src.items import EpisodeItem

# todo make this generic
maxSeasons = 3


class ImdbSpider(scrapy.Spider):
    name = "imdb"

    def __init__(self, domain='', startUrl=''):
        self.start_urls = [startUrl]
        self.allowed_domains = [domain]

    # Extract page url for episode list of next season
    def getNextSeasonRequest(self, response, currentSeasonIndex):
        baseUrl = response.request.url.split('?')[0]
        nextUrl = baseUrl + "?season=" + `(currentSeasonIndex + 1)`
        request = scrapy.Request(nextUrl, self.parse)
        request.meta['seasonIndex'] = currentSeasonIndex + 1
        return request

    # Parse season episode list to extract link for each episode
    def parse(self, response):

        seriesName = response.xpath(
            "//h3[@itemprop='name']/a/text()").extract()
        seriesYears = response.xpath(
            "//h3[@itemprop='name']/span/text()").extract()

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
        if 'seasonIndex' in response.meta:
            seasonIndex = response.meta['seasonIndex']
        else:
            seasonIndex = 1

        print ("Season index extracted is ", seasonIndex)
        if seasonIndex < maxSeasons:
            yield self.getNextSeasonRequest(response, seasonIndex)

    # Parse individual episode page to extract rating
    def parseEpisodePage(self, response):
        episodeRating = response.xpath(
            "//div[@class='imdbRating']/div[@class='ratingValue']/strong/span[@itemprop='ratingValue']/text()").extract()
        numberOfRatings = response.xpath(
            "//div[@class='imdbRating']/a/span[@class='small']/text()").extract()
        completeLink = response.request.url
        # todo extract more info about episode
        description = response.xpath(
            "//div[@class='minPosterWithPlotSummaryHeight']/div[@class='plot_summary_wrapper']/div[@class='plot_summary minPlotHeightWithPoster']/div[@class='summary_text']/text()").extract()
