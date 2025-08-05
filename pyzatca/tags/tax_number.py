"""
Tax Number tag for ZATCA QR code.
"""

from .tag import Tag


class TaxNumber(Tag):
    """
    Tax Number tag (Tag 2) - represents the seller tax number.
    """
    
    def __init__(self, value: str):
        """
        Initialize a TaxNumber tag.
        
        Args:
            value (str): The seller tax number
        """
        super().__init__(2, value) 