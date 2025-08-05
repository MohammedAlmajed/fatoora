"""
Generate QR Code for ZATCA e-invoicing.
"""

import base64
from typing import List, Union
from .tags.tag import Tag


class GenerateQrCode:
    """
    Generate QR codes for ZATCA e-invoicing.
    
    This class handles the generation of QR codes from TLV (Tag-Length-Value) data.
    """
    
    def __init__(self, data: List[Tag]):
        """
        Initialize the QR code generator.
        
        Args:
            data (List[Tag]): List of Tag instances
            
        Raises:
            ValueError: If the data structure is malformed
        """
        self.data = [tag for tag in data if isinstance(tag, Tag)]
        
        if len(self.data) == 0:
            raise ValueError('malformed data structure')
    
    @classmethod
    def from_array(cls, data: List[Tag]) -> 'GenerateQrCode':
        """
        Create a QR code generator from an array of tags.
        
        Args:
            data (List[Tag]): List of Tag instances
            
        Returns:
            GenerateQrCode: A new GenerateQrCode instance
        """
        return cls(data)
    
    def to_tlv(self) -> str:
        """
        Encode the TLV data structure.
        
        Returns:
            str: A string representing the encoded TLV data structure
        """
        return ''.join(str(tag) for tag in self.data)
    
    def to_base64(self) -> str:
        """
        Encode the TLV as base64.
        
        Returns:
            str: The TLV as base64 encoded string
        """
        return base64.b64encode(self.to_tlv().encode('utf-8')).decode('ascii')
    
    def render(self, options: dict = None, file_path: str = None) -> str:
        """
        Render the QR code as base64 data image.
        
        Args:
            options (dict, optional): QR code options
            file_path (str, optional): File path to save the QR code image
            
        Returns:
            str: Base64 encoded PNG image data
        """
        try:
            import qrcode
            from io import BytesIO
            
            # Create QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(self.to_base64())
            qr.make(fit=True)
            
            # Create image
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Convert to base64
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            img_data = base64.b64encode(buffer.getvalue()).decode('ascii')
            
            # Save to file if specified
            if file_path:
                img.save(file_path)
            
            return f"data:image/png;base64,{img_data}"
            
        except ImportError:
            raise ImportError(
                "qrcode library is required for QR code rendering. "
                "Install it with: pip install qrcode[pil]"
            ) 