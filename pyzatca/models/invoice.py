"""
Invoice model for ZATCA.
"""


class Invoice:
    """
    Invoice model for ZATCA e-invoicing.
    
    This class represents an invoice with its XML content and metadata.
    """
    
    def __init__(self, xml_content: str):
        """
        Initialize an invoice.
        
        Args:
            xml_content (str): The invoice XML content
        """
        self.xml_content = xml_content
    
    def get_xml_content(self) -> str:
        """Get the XML content."""
        return self.xml_content
    
    def set_xml_content(self, xml_content: str) -> 'Invoice':
        """Set the XML content."""
        self.xml_content = xml_content
        return self 