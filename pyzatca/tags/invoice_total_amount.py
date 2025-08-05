"""
Invoice Total Amount tag for ZATCA QR code.
"""

from .tag import Tag


class InvoiceTotalAmount(Tag):
    """
    Invoice Total Amount tag (Tag 4) - represents the invoice total amount.
    """
    
    def __init__(self, value: str):
        """
        Initialize an InvoiceTotalAmount tag.
        
        Args:
            value (str): The invoice total amount (e.g., '100.00')
        """
        super().__init__(4, value) 