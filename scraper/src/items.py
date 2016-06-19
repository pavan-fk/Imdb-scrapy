import scrapy


class EpisodeItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    episodeRating = scrapy.Field()
    numberOfRatings = scrapy.Field()
    season = scrapy.Field()
    episode = scrapy.Field()
