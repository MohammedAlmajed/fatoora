"""
Seller tag for ZATCA QR code.
"""

from .tag import Tag


class Seller(Tag):
    """
    Seller tag (Tag 1) - represents the seller name.
    """
    
    def __init__(self, value: str):
        """
        Initialize a Seller tag.
        
        Args:
            value (str): The seller name
        """
        super().__init__(1, value) 