# common/base_model.py

from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class BaseProduct(ABC):
    """Abstract base class for product models."""

    name: str
    price: str
    image_path: str

    @abstractmethod
    def to_dict(self) -> dict[str, str]:
        """Converts the product instance to a dictionary."""
        pass
