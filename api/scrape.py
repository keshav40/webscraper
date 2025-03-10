from fastapi import APIRouter, Query, HTTPException, Header, Depends

from client.scraper_resigtery import get_scraper
from client.dependencies import db, cache

router = APIRouter()


def verify_token(
        x_api_token: str = Header(None), 
        client_name: str = Query(...)
    ):
    """Verifies the API token from headers."""
    
    _, settings = get_scraper(client_name)

    if x_api_token != settings.security_token:
        raise HTTPException(status_code=403, detail="Invalid or missing API token")
    return True

@router.get("/scrape")
def scrape_website(
    client_name: str,
    num_pages: int = Query(1, ge=1, le=10), 
    proxy: str = Query(None, description="Proxy URL"),
    _: bool = Depends(verify_token)
):
    """
    API endpoint to scrape product data from website.
    
    :param num_pages: Number of pages to scrape (default: 1, max: 10).
    :return: List of product data.
    """
    try:
        scraper, _ = get_scraper(client_name, proxy=proxy)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    scraped_data = scraper.scrape(num_pages)
    scraped_products = {"products": [product.to_dict() for product in scraped_data]}

    # print the data collected
    print(f"Scraped products stored in database: {len(scraped_products['products'])}")
    
    # Save data in JSONStorage.
    db.save(scraped_products)
    
    return scraped_products

