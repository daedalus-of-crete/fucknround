from dataclasses import dataclass
from typing import Optional

@dataclass
class AbsProduct:
    title: str
    category: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    url: Optional[str] = None
    last_updated: Optional[str] = None  # or datetime.datetime
    rating: Optional[float] = None
    position: Optional[int] = None
