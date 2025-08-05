#!/usr/bin/env python3
"""
Example: Save QR code as image file.
"""

from pyzatca import GenerateQrCode
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount
import base64


def main():
    """Demonstrate saving QR code as image file."""
    print("ZATCA QR Code Image Saving Example")
    print("=" * 40)
    
    # Generate QR code
    qr_generator = GenerateQrCode.from_array([
        Seller('Salla'),
        TaxNumber('1234567891'),
        InvoiceDate('2021-07-12T14:25:09Z'),
        InvoiceTotalAmount('100.00'),
        InvoiceTaxAmount('15.00')
    ])
    
    # Method 1: Save directly to file using render() method
    qr_image_data = qr_generator.render(file_path='qr_code.png')
    print(f"QR code saved as 'qr_code.png'")
    print(f"Image data: {qr_image_data[:100]}...")
    
    # Method 2: Get base64 data and save manually
    qr_base64 = qr_generator.to_base64()
    print(f"\nQR code base64: {qr_base64}")
    
    # Method 3: Get TLV string
    tlv_string = qr_generator.to_tlv()
    print(f"\nTLV string: {tlv_string}")
    
    # Method 4: Generate QR code with Arabic text
    arabic_qr = GenerateQrCode.from_array([
        Seller('سلة'),
        TaxNumber('1234567891'),
        InvoiceDate('2021-07-12T14:25:09Z'),
        InvoiceTotalAmount('100.00'),
        InvoiceTaxAmount('15.00')
    ])
    
    arabic_qr.render(file_path='arabic_qr_code.png')
    print(f"\nArabic QR code saved as 'arabic_qr_code.png'")


if __name__ == "__main__":
    main() 