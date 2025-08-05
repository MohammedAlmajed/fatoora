"""
Certificate Signature tag for ZATCA QR code.
"""

from .tag import Tag


class CertificateSignature(Tag):
    """
    Certificate Signature tag (Tag 8) - represents the certificate signature.
    """
    
    def __init__(self, value: str):
        """
        Initialize a CertificateSignature tag.
        
        Args:
            value (str): The certificate signature
        """
        super().__init__(8, value) 