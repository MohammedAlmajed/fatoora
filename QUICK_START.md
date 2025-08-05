# Quick Start - Generate QR Code in 5 Minutes

## 🚀 Step 1: Clone and Install

```bash
# Clone the repository
git clone https://github.com/yourusername/pyzatca.git
cd pyzatca

# Install basic dependencies (required)
pip install cryptography

# Install QR code library (optional, for image generation)
pip install qrcode[pil]

# Install the package
pip install -e .
```

## 🎯 Step 2: Generate Your First QR Code

Create a file called `my_first_qr.py`:

```python
#!/usr/bin/env python3
"""
My First ZATCA QR Code
"""

from pyzatca import GenerateQrCode
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount

# Your company information
company_name = "Your Company Name"
vat_number = "123456789012345"
amount = 100.00
tax_amount = 15.00

# Generate QR code
qr_generator = GenerateQrCode.from_array([
    Seller(company_name),
    TaxNumber(vat_number),
    InvoiceDate('2025-08-05T07:21:06Z'),
    InvoiceTotalAmount(f"{amount:.2f}"),
    InvoiceTaxAmount(f"{tax_amount:.2f}")
])

# Save as image
qr_generator.render(file_path='my_first_qr.png')

# Get base64 data
qr_base64 = qr_generator.to_base64()

print("✅ QR Code Generated Successfully!")
print(f"📁 Saved as: my_first_qr.png")
print(f"📋 Base64: {qr_base64}")
print(f"💰 Amount: {amount} SAR")
print(f"🏢 Company: {company_name}")
```

## 🏃‍♂️ Step 3: Run It!

```bash
python my_first_qr.py
```

## 📱 Step 4: View Your QR Code

- Open `my_first_qr.png` in any image viewer
- Or scan it with your phone's camera
- The QR code contains your invoice data in ZATCA format

## 🔧 Customize for Your Company

Edit the variables in `my_first_qr.py`:

```python
# Change these to your company details
company_name = "شركة حدث لتقنية المعلومات"  # Your company name
vat_number = "312087593400003"              # Your VAT number
amount = 500.00                             # Invoice amount
tax_amount = 75.00                          # Tax amount
```

## 🌐 Generate HTML QR Code

Want to display the QR code on a website? Use this:

```python
from pyzatca import GenerateQrCode
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount

qr_generator = GenerateQrCode.from_array([
    Seller('Your Company'),
    TaxNumber('123456789012345'),
    InvoiceDate('2025-08-05T07:21:06Z'),
    InvoiceTotalAmount('100.00'),
    InvoiceTaxAmount('15.00')
])

# Get HTML data URL
data_url = qr_generator.render()

# Create HTML file
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>ZATCA QR Code</title>
</head>
<body>
    <h1>Your Invoice QR Code</h1>
    <img src="{data_url}" alt="ZATCA QR Code" />
</body>
</html>
"""

with open('qr_code.html', 'w') as f:
    f.write(html_content)

print("✅ HTML file created: qr_code.html")
print("🌐 Open qr_code.html in your browser")
```

## 🧪 Test the Examples

```bash
# Run the included examples
python examples/basic_usage.py
python examples/save_qr_image.py
python examples/qr_code_display.py
```

## 📚 Next Steps

- Read `USAGE.md` for advanced features
- Check `README.md` for complete documentation
- Run `pytest` to verify everything works
- Generate CSR for ZATCA registration

## 🆘 Need Help?

- Check the `examples/` directory for more examples
- Read `USAGE.md` for detailed documentation
- Open an issue on GitHub if you have problems

---

**That's it! You now have a working ZATCA QR code generator! 🎉** 