"""
Invoice Date tag for ZATCA QR code.
"""

from .tag import Tag


class InvoiceDate(Tag):
    """
    Invoice Date tag (Tag 3) - represents the invoice date in ISO8601 format.
    """
    
    def __init__(self, value: str):
        """
        Initialize an InvoiceDate tag.
        
        Args:
            value (str): The invoice date in ISO8601 format (e.g., '2021-07-12T14:25:09Z')
        """
        super().__init__(3, value) 