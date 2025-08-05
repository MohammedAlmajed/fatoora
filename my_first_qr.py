#!/usr/bin/env python3
"""
My First ZATCA QR Code - Run this after cloning!
"""

from pyzatca import GenerateQrCode
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount

def main():
    """Generate your first ZATCA QR code."""
    print("🎉 Welcome to ZATCA Python Library!")
    print("=" * 40)
    
    # Your company information (change these!)
    company_name = "Your Company Name"
    vat_number = "123456789012345"
    amount = 100.00
    tax_amount = 15.00
    
    print(f"🏢 Company: {company_name}")
    print(f"📋 VAT Number: {vat_number}")
    print(f"💰 Amount: {amount} SAR")
    print(f"🏛️ Tax Amount: {tax_amount} SAR")
    print()
    
    # Generate QR code
    qr_generator = GenerateQrCode.from_array([
        Seller(company_name),
        TaxNumber(vat_number),
        InvoiceDate('2025-08-05T07:21:06Z'),
        InvoiceTotalAmount(f"{amount:.2f}"),
        InvoiceTaxAmount(f"{tax_amount:.2f}")
    ])
    
    # Get base64 data (this works without qrcode library)
    qr_base64 = qr_generator.to_base64()
    
    print("✅ QR Code Generated Successfully!")
    print(f"📋 Base64: {qr_base64}")
    print()
    print("📱 To save as image, install qrcode library:")
    print("   pip install qrcode[pil]")
    print()
    print("🔧 To customize:")
    print("   - Edit the variables in this file")
    print("   - Change company name, VAT number, amounts")
    print("   - Run again to generate new QR codes")
    print()
    print("📚 For more examples, see:")
    print("   - examples/basic_usage.py")
    print("   - examples/save_qr_image.py")
    print("   - examples/qr_code_display.py")
    print("   - USAGE.md for detailed documentation")
    print()
    print("🎯 Next steps:")
    print("   1. Install: pip install qrcode[pil]")
    print("   2. Run: python examples/basic_usage.py")
    print("   3. Read: QUICK_START.md")


if __name__ == "__main__":
    main() 