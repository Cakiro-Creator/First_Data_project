# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# Import the scrapy module to use its Item and Field classes
import scrapy


# Define the item class for NHL team data
# This class represents the structure of data we'll extract from each team record
# Using scrapy.Item provides validation, serialization, and other benefits
class NhlscraperItem(scrapy.Item):
    # Each field corresponds to a column in the NHL data table
    # scrapy.Field() creates a field descriptor for storing extracted data

    # Team name (e.g., "Boston Bruins")
    Team_Name = scrapy.Field()

    # Season year (e.g., "1990")
    Year = scrapy.Field()

    # Number of regular season wins
    Wins = scrapy.Field()

    # Number of regular season losses
    Losses = scrapy.Field()

    # Number of overtime/shootout losses
    Overtime_Losses = scrapy.Field()

    # Win percentage (decimal, e.g., "0.573")
    Win_Percentage = scrapy.Field()

    # Total goals scored for
    Goals_For = scrapy.Field()

    # Total goals scored against
    Goals_Against = scrapy.Field()

    # Goal differential (+/- goals)
    Goal_Differential = scrapy.Field()

    # Note: Additional fields can be added here if the data source expands
    # The 'pass' statement is Python syntax for an empty block
    pass
