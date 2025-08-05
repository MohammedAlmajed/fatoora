"""
Base Tag class for TLV (Tag-Length-Value) encoding used in ZATCA QR codes.
"""

import struct


class Tag:
    """
    Base class for TLV (Tag-Length-Value) encoding.
    
    Each tag has a tag number, a value, and automatically calculates the length.
    """
    
    def __init__(self, tag: int, value):
        """
        Initialize a Tag instance.
        
        Args:
            tag (int): The tag number
            value: The value to encode
        """
        self.tag = tag
        self.value = str(value)
    
    def get_tag(self) -> int:
        """Get the tag number."""
        return self.tag
    
    def get_value(self) -> str:
        """Get the tag value."""
        return self.value
    
    def get_length(self) -> int:
        """
        Get the length of the value in bytes.
        
        Important: Returns the number of bytes of the string, not the number of characters.
        """
        return len(self.value.encode('utf-8'))
    
    def to_hex(self, value: int) -> bytes:
        """
        Convert a value to hex representation.
        
        Args:
            value (int): The value to convert
            
        Returns:
            bytes: The hex representation
        """
        return struct.pack("B", value)
    
    def __str__(self) -> str:
        """
        Convert the tag to its TLV string representation.
        
        Returns:
            str: The TLV encoded string
        """
        value = str(self.get_value())
        return (
            self.to_hex(self.get_tag()).decode('latin1') +
            self.to_hex(self.get_length()).decode('latin1') +
            value
        )
    
    def __repr__(self) -> str:
        return f"Tag(tag={self.tag}, value='{self.value}')" 