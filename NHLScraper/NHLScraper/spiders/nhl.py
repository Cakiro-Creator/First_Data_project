# NHLScraper Spider for scraping NHL team statistics from scrapethissite.com
#
# This spider crawls the NHL team data page, extracts team statistics from the table,
# and handles pagination to scrape all available data.
#
# Usage:
#   scrapy crawl nhlscraper -o output.csv
#
# This will scrape all NHL team records and save them to a CSV file.
#
# Why this structure?
# - We use CSS selectors to target table rows and cells for reliable data extraction.
# - Pagination is handled by following the "Next" link with aria-label.
# - Data is yielded as dictionaries for easy CSV export.
# - The spider respects robots.txt and uses delays to be respectful to the site.

import scrapy


class NhlscraperSpider(scrapy.Spider):
    # Spider name used in command line: scrapy crawl nhlscraper
    # This must be unique across all spiders in the project
    name = "nhlscraper"

    # Starting URLs for the crawl
    # We start with page 1, showing 100 records per page to minimize requests
    start_urls = [
        "https://www.scrapethissite.com/pages/forms/?page_num=1&per_page=100",
    ]

    def parse(self, response):
        # Main parsing method called for each page response
        # The data is presented in an HTML table with class "table"

        # Select all table rows, skipping the first (header) row
        # response.css() uses CSS selectors to find elements
        rows = response.css("table.table tr")[1:]  # Skip header row

        # Iterate through each data row
        for row in rows:
            # Extract all table data cells in this row
            tds = row.css("td")

            # Ensure we have at least 9 columns (all expected fields)
            # This prevents errors if the table structure changes
            if len(tds) >= 9:
                # Extract text from each cell and strip whitespace
                # ::text gets the text content of the element
                # .strip() removes leading/trailing whitespace
                yield {
                    "Team_Name": tds[0].css("::text").get().strip(),
                    "Year": tds[1].css("::text").get().strip(),
                    "Wins": tds[2].css("::text").get().strip(),
                    "Losses": tds[3].css("::text").get().strip(),
                    "Overtime_Losses": tds[4].css("::text").get().strip(),
                    "Win_Percentage": tds[5].css("::text").get().strip(),
                    "Goals_For": tds[6].css("::text").get().strip(),
                    "Goals_Against": tds[7].css("::text").get().strip(),
                    "Goal_Differential": tds[8].css("::text").get().strip(),
                }

        # Handle pagination: find the "Next" page link
        # aria-label="Next" targets the pagination link specifically
        # ::attr(href) extracts the href attribute value
        next_page = response.css('a[aria-label="Next"]::attr(href)').get()

        # If there's a next page, follow it and call parse again
        # response.follow() creates a new request with the same callback
        if next_page is not None:
            yield response.follow(next_page, self.parse)
