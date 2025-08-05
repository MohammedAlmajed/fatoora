"""
Public Key tag for ZATCA QR code.
"""

from .tag import Tag


class PublicKey(Tag):
    """
    Public Key tag (Tag 7) - represents the public key.
    """
    
    def __init__(self, value: str):
        """
        Initialize a PublicKey tag.
        
        Args:
            value (str): The public key
        """
        super().__init__(7, value) 