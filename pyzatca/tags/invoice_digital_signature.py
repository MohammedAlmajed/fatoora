"""
Invoice Digital Signature tag for ZATCA QR code.
"""

from .tag import Tag


class InvoiceDigitalSignature(Tag):
    """
    Invoice Digital Signature tag (Tag 6) - represents the invoice digital signature.
    """
    
    def __init__(self, value: str):
        """
        Initialize an InvoiceDigitalSignature tag.
        
        Args:
            value (str): The invoice digital signature
        """
        super().__init__(6, value) 