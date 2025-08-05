"""
CSR model for ZATCA.
"""


class CSR:
    """
    Certificate Signing Request (CSR) model.
    
    This class holds the CSR content and private key generated
    for ZATCA e-invoicing integration.
    """
    
    def __init__(self, csr_content: str, private_key):
        """
        Initialize a CSR instance.
        
        Args:
            csr_content (str): The CSR content as a string
            private_key: The private key object
        """
        self.csr_content = csr_content
        self.private_key = private_key
    
    def get_csr_content(self) -> str:
        """Get the CSR content."""
        return self.csr_content
    
    def get_private_key(self):
        """Get the private key."""
        return self.private_key 