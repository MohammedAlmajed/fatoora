"""
Invoice Tax Amount tag for ZATCA QR code.
"""

from .tag import Tag


class InvoiceTaxAmount(Tag):
    """
    Invoice Tax Amount tag (Tag 5) - represents the invoice tax amount.
    """
    
    def __init__(self, value: str):
        """
        Initialize an InvoiceTaxAmount tag.
        
        Args:
            value (str): The invoice tax amount (e.g., '15.00')
        """
        super().__init__(5, value) 