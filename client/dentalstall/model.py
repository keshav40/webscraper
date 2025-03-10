from client.core.model import BaseProduct

class DentalstallProduct(BaseProduct):
    """Model representing a product scraped from Dentalstall."""

    def to_dict(self) -> dict[str, str]:
        return {
            "name": self.name,
            "price": self.price,
            "image_path": self.image_path,
        }
