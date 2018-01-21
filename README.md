# Imdb-scrapy
My attempt to clone the effort at [GraphTV](http://graphtv.kevinformatics.com/)

tldr; Plot the ratings of all episodes of a TV series

## Why?
- This project is helping me learn Python
- GraphTV does not have all the series I want to look up

## How?
The tech I have used:
- To scrap IMDB for ratings - [Scrapy](http://scrapy.org/)
- For the Website - [Flask](http://flask.pocoo.org/)
- To plot the graph - Currently [CanvasJS](http://canvasjs.com/assets/script/canvasjs.min.js). Exploring other options as I can think of different kinds of visualization.

Version 1 screen shot
![image](http://i.imgur.com/83fgbxj.png)


## Project Structure
There are 3 folders
- data: Contains the data scraped from the website.
        Could possibly contain a database and a format that the graphing library can take in directly
        
- scraper: Scrapy based scraper

- website: Flask based website