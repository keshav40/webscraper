import os
import requests
from bs4 import BeautifulSoup

from client.utils import download_image
from client.core.scraper import BaseScraper
from client.dentalstall.model import DentalstallProduct


class DentalstallScraper(BaseScraper):
    """Scraper for Dentalstall website."""

    def __init__(self, base_url: str, cache=None, proxy=None):
        super().__init__(base_url, cache, proxy)
    
    def parse(self, html_content: str) -> list[DentalstallProduct]:
        """
        Parses the HTML content and extracts product details.

        :param html_content: The raw HTML content of the page.
        :return: A list of DentalstallProduct objects.
        """
        soup = BeautifulSoup(html_content, "html.parser")
        products = []
        for product in soup.select(".product-inner"):
            name = product.select_one(".woo-loop-product__title").get_text(strip=True)
            price = product.select_one(".woocommerce-Price-amount").get_text(strip=True)
            image_url = (
                product.select_one(".mf-product-thumbnail img").get('data-lazy-src', None) 
                if product.select_one(".mf-product-thumbnail img") 
                else None
            )
            filename = os.path.join("images", image_url.split("/")[-1])

            cached_entry = self.cache.get(name)
            if cached_entry and cached_entry.get("price") == price:
                path_to_image = filename
            else:
                path_to_image = download_image(url=image_url, filename=filename)
                product_data = {
                    "name": name,
                    "price": price,
                    "image_path": path_to_image
                }
                self.cache.set(name, product_data)

            product_obj = DentalstallProduct(name=name, price=price, image_path=path_to_image)
            products.append(product_obj)

        return products

    def scrape(self, num_pages: int) -> list[dict[str, str]]:
        """
        Scrapes multiple pages from the Dentalstall website.
        :param num_pages: Number of pages to scrape.
        :return: List of extracted product data.
        """
        scraped_data = []
        for page in range(1, num_pages + 1):
            url = self.base_url.format(page)
            html_content = self.fetch_page(url)
            if html_content:
                parsed_data = self.parse(html_content)
                scraped_data.extend(parsed_data)
        return scraped_data
