#!/usr/bin/env python3
"""
Basic usage example for pyzatca library.

This example demonstrates how to generate QR codes for ZATCA e-invoicing.
"""

from pyzatca import GenerateQrCode
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount


def main():
    """Demonstrate basic QR code generation."""
    print("ZATCA QR Code Generation Example")
    print("=" * 40)
    
    # Create QR code from tags
    qr_code = GenerateQrCode.from_array([
        Seller('Salla'),                    # seller name
        TaxNumber('1234567891'),            # seller tax number
        InvoiceDate('2021-07-12T14:25:09Z'), # invoice date as Zulu ISO8601
        InvoiceTotalAmount('100.00'),       # invoice total amount
        InvoiceTaxAmount('15.00')           # invoice tax amount
    ]).to_base64()
    
    print(f"Generated QR Code (Base64): {qr_code}")
    
    # Generate QR code image
    qr_image_data = GenerateQrCode.from_array([
        Seller('Salla'),
        TaxNumber('1234567891'),
        InvoiceDate('2021-07-12T14:25:09Z'),
        InvoiceTotalAmount('100.00'),
        InvoiceTaxAmount('15.00')
    ]).render()
    
    print(f"\nQR Code Image Data: {qr_image_data[:100]}...")
    
    # Generate TLV string
    tlv_string = GenerateQrCode.from_array([
        Seller('Salla'),
        TaxNumber('1234567891'),
        InvoiceDate('2021-07-12T14:25:09Z'),
        InvoiceTotalAmount('100.00'),
        InvoiceTaxAmount('15.00')
    ]).to_tlv()
    
    print(f"\nTLV String: {tlv_string}")
    
    # Example with Arabic text
    arabic_qr = GenerateQrCode.from_array([
        Seller('سلة'),
        TaxNumber('1234567891'),
        InvoiceDate('2021-07-12T14:25:09Z'),
        InvoiceTotalAmount('100.00'),
        InvoiceTaxAmount('15.00')
    ]).to_base64()
    
    print(f"\nArabic QR Code (Base64): {arabic_qr}")


if __name__ == "__main__":
    main() 