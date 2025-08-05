#!/usr/bin/env python3
"""
Example: Different ways to display QR codes.
"""

from pyzatca import GenerateQrCode
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount
import base64


def main():
    """Demonstrate different ways to display QR codes."""
    print("ZATCA QR Code Display Examples")
    print("=" * 40)
    
    # Generate QR code
    qr_generator = GenerateQrCode.from_array([
        Seller('Salla'),
        TaxNumber('1234567891'),
        InvoiceDate('2021-07-12T14:25:09Z'),
        InvoiceTotalAmount('100.00'),
        InvoiceTaxAmount('15.00')
    ])
    
    # Method 1: Get base64 data (for embedding in HTML)
    qr_base64 = qr_generator.to_base64()
    print(f"1. Base64 data: {qr_base64}")
    
    # Method 2: Get data URL (for HTML img src)
    qr_data_url = qr_generator.render()
    print(f"\n2. Data URL: {qr_data_url[:100]}...")
    
    # Method 3: Save to file
    qr_generator.render(file_path='qr_code_display.png')
    print(f"\n3. Saved as file: qr_code_display.png")
    
    # Method 4: Get TLV string
    tlv_string = qr_generator.to_tlv()
    print(f"\n4. TLV string: {tlv_string}")
    
    # Method 5: HTML example
    html_example = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>ZATCA QR Code</title>
    </head>
    <body>
        <h1>ZATCA QR Code</h1>
        <img src="{qr_data_url}" alt="ZATCA QR Code" />
        <p>Base64: {qr_base64}</p>
    </body>
    </html>
    """
    
    with open('qr_code_example.html', 'w') as f:
        f.write(html_example)
    
    print(f"\n5. HTML file created: qr_code_example.html")
    print(f"   Open this file in a browser to see the QR code")


if __name__ == "__main__":
    main() 