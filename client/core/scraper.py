# common/base_scraper.py
from abc import ABC, abstractmethod
import requests
from time import sleep


class BaseScraper(ABC):
    """Abstract base class for scrapers."""

    def __init__(self, base_url: str, cache=None, proxy=None):
        """
        Initializes the scraper.
        """
        self.base_url = base_url
        self.cache = cache
        self.session = requests.Session()
        if proxy:
            self.session.proxies = {"http": proxy, "https": proxy}
        
        self.max_retries = 3
        self.delay = 2

    def fetch_page(self, url: str) -> str:
        """Fetches the webpage and returns its HTML content."""
        for attempt in range(self.max_retries):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                return response.text
            except requests.RequestException as e:
                print(f"Error fetching {url}: {e}. Retrying {attempt+1}/{self.max_retries}...")
                sleep(self.delay)
        return ""
    
    @abstractmethod
    def parse(self, html_content: str) -> list[dict[str, str]]:
        """
        """
        pass

    @abstractmethod
    def scrape(self, num_pages: int) -> list[dict[str, str]]:
        """
        Scrapes data from multiple pages.
        :param num_pages: Number of pages to scrape.
        :return: List of product dictionaries.
        """
        pass
