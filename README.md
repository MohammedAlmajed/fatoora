# ZATCA (Fatoora) QR-Code Implementation for Python

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/badge/pypi-pyzatca-blue.svg)](https://pypi.org/project/pyzatca/)

A Python port of the original [ZATCA PHP library](https://github.com/SallaApp/ZATCA) by Salla. This package helps developers implement ZATCA (Fatoora) QR code easily, which is required for Saudi Arabia's e-invoicing system.

## Features

- ✅ Generate CSR (Certificate Signing Request) for ZATCA integration
- ✅ Generate QR codes for e-invoices (Phase 1 and Phase 2)
- ✅ Support for TLV (Tag-Length-Value) encoding
- ✅ Invoice signing and digital signature generation
- ✅ Certificate management and validation
- ✅ Support for all ZATCA environments (sandbox, simulation, production)
- ✅ Full Arabic text support

## Requirements

- Python >= 3.7
- cryptography >= 3.4.8
- qrcode[pil] >= 7.3.1

## 🚀 Quick Start (5 Minutes)

### Step 1: Clone and Install
```bash
git clone https://github.com/yourusername/pyzatca.git
cd pyzatca

# Install basic dependencies (required)
pip install cryptography

# Install QR code library (optional, for image generation)
pip install qrcode[pil]

# Install the package
pip install -e .
```

### Step 2: Generate Your First QR Code
Create `my_first_qr.py`:
```python
from pyzatca import GenerateQrCode
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount

# Generate QR code
qr_generator = GenerateQrCode.from_array([
    Seller('Your Company Name'),
    TaxNumber('123456789012345'),
    InvoiceDate('2025-08-05T07:21:06Z'),
    InvoiceTotalAmount('100.00'),
    InvoiceTaxAmount('15.00')
])

# Save as image
qr_generator.render(file_path='my_first_qr.png')
print("✅ QR Code saved as 'my_first_qr.png'")
```

### Step 3: Run It!
```bash
python my_first_qr.py
```

**That's it!** You now have a working ZATCA QR code generator! 🎉

📖 **For detailed instructions, see [QUICK_START.md](QUICK_START.md)**

## Installation

You can install the package via pip:

```bash
pip install pyzatca
```

Or install from source:

```bash
git clone https://github.com/example/pyzatca.git
cd pyzatca
pip install -e .
```

## Quick Start

### Generate QR Code

```python
from pyzatca import GenerateQrCode
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount

# Generate QR code
qr_code = GenerateQrCode.from_array([
    Seller('شركة حدث لتقنية المعلومات'),
    TaxNumber('312087593400003'),
    InvoiceDate('2025-08-05T07:21:06Z'),
    InvoiceTotalAmount('100.00'),
    InvoiceTaxAmount('15.00')
]).to_base64()

print(qr_code)
# Output: AS/YtNix2YPYqSDYrdiv2Ksg2YTYqtmC2YbZitipINin2YTZhdi52YTZiNmF2KfYqgIPMzEyMDg3NTkzNDAwMDAzAxQyMDI1LTA4LTA1VDA3OjIxOjA2WgQGMTAwLjAwBQUxNS4wMA==
```

### Generate CSR for ZATCA

```python
from pyzatca import GenerateCSR, CSRRequest

# Create CSR request
csr_request = (CSRRequest.make()
    .set_uid('312087593400003')  # Your VAT number
    .set_serial_number('MySolution', '1.0', '123456789')
    .set_common_name('شركة حدث لتقنية المعلومات')
    .set_country_name('SA')
    .set_organization_name('شركة حدث لتقنية المعلومات')
    .set_invoice_type(True, True)  # Tax and Simplified invoices
    .set_current_zatca_env('sandbox'))

# Generate CSR
csr = GenerateCSR.from_request(csr_request).initialize().generate()

# Save CSR for submission to ZATCA
with open('csr.pem', 'w') as f:
    f.write(csr.get_csr_content())
```

### Generate QR Code Image

```python
from pyzatca import GenerateQrCode
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount

# Generate and save QR code image
qr_generator = GenerateQrCode.from_array([
    Seller('شركة حدث لتقنية المعلومات'),
    TaxNumber('312087593400003'),
    InvoiceDate('2025-08-05T07:21:06Z'),
    InvoiceTotalAmount('100.00'),
    InvoiceTaxAmount('15.00')
])

# Save as PNG file
qr_generator.render(file_path='invoice_qr.png')

# Get data URL for HTML
data_url = qr_generator.render()
print(f"HTML: <img src='{data_url}' alt='QR Code' />")
```

## Usage Examples

### Basic QR Code Generation

```python
from pyzatca import GenerateQrCode
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount

# Generate QR code from tags
qr_code = GenerateQrCode.from_array([
    Seller('Salla'),                    # seller name
    TaxNumber('1234567891'),            # seller tax number
    InvoiceDate('2021-07-12T14:25:09Z'), # invoice date as Zulu ISO8601
    InvoiceTotalAmount('100.00'),       # invoice total amount
    InvoiceTaxAmount('15.00')           # invoice tax amount
]).to_base64()

print(qr_code)
# Output: AQVTYWxsYQIKMTIzNDU2Nzg5MQMUMjAyMS0wNy0xMlQxNDoyNTowOVoEBjEwMC4wMAUFMTUuMDA=
```

### Certificate Management

```python
from pyzatca import Certificate

# Load certificate (you'll get these from ZATCA)
certificate = Certificate(
    'certificate_plain_text',  # From ZATCA
    'private_key_plain_text'   # Your private key
).set_secret_key('secret_key_text')  # From ZATCA

# Generate authorization header
auth_header = certificate.get_authorization_header()
print(auth_header)
```

## API Reference

### Classes

#### `GenerateCSR`
Generates Certificate Signing Requests for ZATCA integration.

#### `GenerateQrCode`
Generates QR codes from TLV (Tag-Length-Value) data.

#### `CSRRequest`
Model for CSR request data with validation.

#### `Certificate`
Helper class for certificate operations.

#### `InvoiceSign`
Handles invoice signing and QR code generation.

#### Tag Classes
- `Seller` - Seller name (Tag 1)
- `TaxNumber` - Seller tax number (Tag 2)
- `InvoiceDate` - Invoice date (Tag 3)
- `InvoiceTotalAmount` - Invoice total amount (Tag 4)
- `InvoiceTaxAmount` - Invoice tax amount (Tag 5)
- `InvoiceHash` - Invoice hash (Tag 5)
- `InvoiceDigitalSignature` - Invoice digital signature (Tag 6)
- `PublicKey` - Public key (Tag 7)
- `CertificateSignature` - Certificate signature (Tag 8)

## Testing

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run tests with coverage
pytest --cov=pyzatca
```

## Development

```bash
# Install in development mode
pip install -e .

# Format code
black pyzatca/

# Lint code
flake8 pyzatca/

# Type checking
mypy pyzatca/
```

## ZATCA Integration Process

1. **Register on ZATCA Portal**: https://zatca.gov.sa
2. **Generate CSR**: Use this library to create certificate signing request
3. **Submit CSR**: Send to ZATCA via their APIs
4. **Receive Certificate**: Get digital certificate and secret key from ZATCA
5. **Implement Signing**: Use certificate to sign invoices
6. **Generate QR Codes**: Use this library for compliant QR codes
7. **Submit Invoices**: Send signed invoices to ZATCA

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

- Original PHP library by [Salla](https://github.com/SallaApp/ZATCA)
- Python port by the community

## Support

If you have any questions or need help, please open an issue on GitHub or contact the maintainers.

## Disclaimer

This is an unofficial Python port of the original ZATCA PHP library. It is not officially endorsed by ZATCA or Salla. Please ensure compliance with ZATCA's official documentation and requirements for production use. 