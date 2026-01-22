# Scrapy settings for NHLScraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# Name of the bot (used in user-agent and logging)
BOT_NAME = "NHLScraper"

# Modules where Scrapy will look for spiders
SPIDER_MODULES = ["NHLScraper.spiders"]
# Module where new spiders are created by default
NEWSPIDER_MODULE = "NHLScraper.spiders"

# Add-ons configuration (empty for basic setup)
ADDONS = {}

# Logging level: INFO shows important messages without being too verbose
LOG_LEVEL = "INFO"

# User agent string: identifies your crawler to websites
# Including the target URL shows respect and transparency
USER_AGENT = (
    "NHLScraper (https://www.scrapethissite.com/pages/forms/?page_num=1&per_page=100)"
)

# Respect robots.txt files to crawl ethically
ROBOTSTXT_OBEY = True

# Concurrency and throttling settings
# Limit concurrent requests per domain to 1 to be respectful
CONCURRENT_REQUESTS_PER_DOMAIN = 1
# Add 1 second delay between requests to avoid overwhelming the server
DOWNLOAD_DELAY = 1

# Randomize download delay to mimic human browsing behavior
RANDOMIZE_DOWNLOAD_DELAY = True

# Commented out: global concurrent requests limit (unlimited by default)
# CONCURRENT_REQUESTS = 16

# Commented out: disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Commented out: disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Commented out: custom request headers (using defaults)
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Commented out: spider middlewares (none used in this project)
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "NHLScraper.middlewares.NhlscraperSpiderMiddleware": 543,
# }

# Commented out: downloader middlewares (none used in this project)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "NHLScraper.middlewares.NhlscraperDownloaderMiddleware": 543,
# }

# Commented out: extensions (none used)
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Commented out: item pipelines (none used in this simple project)
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "NHLScraper.pipelines.NhlscraperPipeline": 300,
# }

# Commented out: AutoThrottle extension (disabled)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Commented out: HTTP caching (disabled)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Ensure exported data uses UTF-8 encoding for international characters
FEED_EXPORT_ENCODING = "utf-8"

# Default output file for this project
# Saves scraped items to data/raw/nhl.csv in the main project folder
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
FEEDS = {
    str(_PROJECT_ROOT / "data" / "raw" / "nhl.csv"): {
        "format": "csv",
        "overwrite": True,
    },
}
