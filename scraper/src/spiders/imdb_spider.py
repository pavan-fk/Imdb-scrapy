import scrapy

from src.items import EpisodeItem

# todo make this generic
maxSeasons = 3


class ImdbSpider(scrapy.Spider):
    name = "imdb"

    def __init__(self, domain='', startUrl=''):
        self.start_urls = [startUrl]
        self.allowed_domains = ["imdb.com"]

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
            yield scrapy.Request(
                "http://www.imdb.com" + infoDiv.xpath("strong/a/@href").extract()[0], self.parseEpisodePage)

        # The next page to follow will have ?episodes=n url param
        # todo: Find number of seasons from drop down at the top of the page
        if 'seasonIndex' in response.meta:
            seasonIndex = response.meta['seasonIndex']
        else:
            seasonIndex = 1

        if seasonIndex < maxSeasons:
            yield self.getNextSeasonRequest(response, seasonIndex)

    # Parse individual episode page to extract rating
    def parseEpisodePage(self, response):
        episode = EpisodeItem()
        episode["episodeRating"] = response.xpath(
            "//div[@class='imdbRating']/div[@class='ratingValue']/strong/span[@itemprop='ratingValue']/text()").extract()[0]
        episode["numberOfRatings"] = response.xpath(
            "//div[@class='imdbRating']/a/span[@class='small']/text()").extract()[0]
        episode["link"] = response.request.url
        # todo extract more info about episode
        episode["description"] = response.xpath(
            "//div[@class='minPosterWithPlotSummaryHeight']/div[@class='plot_summary_wrapper']/div[@class='plot_summary minPlotHeightWithPoster']/div[@class='summary_text']/text()").extract()[0].strip()
        episode["title"] = response.xpath(
            "//div[@class='title_wrapper']/h1[@itemprop='name']/text()").extract()[0].strip()
        episode["season"] = response.xpath(
            "//div[@class='button_panel navigation_panel']//div[@class='bp_heading']/text()").extract()[0].split()[1]
        episode["episode"] = response.xpath(
            "//div[@class='button_panel navigation_panel']//div[@class='bp_heading']/text()").extract()[1].split()[1]
        yield episode
