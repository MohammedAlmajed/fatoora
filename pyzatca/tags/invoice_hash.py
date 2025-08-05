"""
Invoice Hash tag for ZATCA QR code.
"""

from .tag import Tag


class InvoiceHash(Tag):
    """
    Invoice Hash tag (Tag 5) - represents the invoice hash.
    """
    
    def __init__(self, value: str):
        """
        Initialize an InvoiceHash tag.
        
        Args:
            value (str): The invoice hash
        """
        super().__init__(5, value) 