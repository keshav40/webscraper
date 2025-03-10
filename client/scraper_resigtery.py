from client.dentalstall.scraper import DentalstallScraper
from settings.settings import DentalstallSettings
from client import dependencies


# Register scrapers and their corresponding settings
SCRAPER_REGISTRY = {
    "dentalstall": (DentalstallScraper, DentalstallSettings),
}

def get_scraper(client_name, proxy=None):
    """
    Fetch the scraper and settings for a given client.
    
    :param client_name: Name of the website (e.g., "dentalstall").
    :return: Scraper instance and settings instance.
    """
    if client_name not in SCRAPER_REGISTRY:
        raise ValueError(f"Scraper for '{client_name}' not registered.")
    
    scraper_class, settings_class = SCRAPER_REGISTRY[client_name]
    settings = settings_class()
    scraper = scraper_class(
        base_url=settings.base_url, 
        cache=dependencies.cache, 
        proxy=proxy
    )
    
    return scraper, settings
