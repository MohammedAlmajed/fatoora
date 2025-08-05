# ZATCA Python Library - Usage Guide

## 🚀 Quick Start

### Installation

```bash
# Install from GitHub
pip install git+https://github.com/yourusername/pyzatca.git

# Or install locally
git clone https://github.com/yourusername/pyzatca.git
cd pyzatca
pip install -e .
```

### Basic QR Code Generation

```python
from pyzatca import GenerateQrCode
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount

# Generate QR code
qr_code = GenerateQrCode.from_array([
    Seller('Your Company Name'),
    TaxNumber('123456789012345'),
    InvoiceDate('2025-08-05T07:21:06Z'),
    InvoiceTotalAmount('100.00'),
    InvoiceTaxAmount('15.00')
]).to_base64()

print(qr_code)
```

## 📋 Complete Examples

### 1. Generate QR Code for Invoice

```python
from pyzatca import GenerateQrCode
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount
from datetime import datetime, timezone

# Invoice data
company_name = "Your Company Name"
vat_number = "123456789012345"
amount = 100.00
tax_amount = 15.00
invoice_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# Generate QR code
qr_generator = GenerateQrCode.from_array([
    Seller(company_name),
    TaxNumber(vat_number),
    InvoiceDate(invoice_date),
    InvoiceTotalAmount(f"{amount:.2f}"),
    InvoiceTaxAmount(f"{tax_amount:.2f}")
])

# Get base64 encoded QR code
qr_base64 = qr_generator.to_base64()
print(f"QR Code: {qr_base64}")

# Save as image
qr_generator.render(file_path='invoice_qr.png')

# Get HTML data URL
data_url = qr_generator.render()
print(f"HTML: <img src='{data_url}' alt='QR Code' />")
```

### 2. Generate CSR for ZATCA Registration

```python
from pyzatca import GenerateCSR, CSRRequest

# Create CSR request
csr_request = (CSRRequest.make()
    .set_uid('123456789012345')  # Your VAT number
    .set_serial_number('MyApp', '1.0', '123456789')
    .set_common_name('Your Company Name')
    .set_country_name('SA')
    .set_organization_name('Your Organization')
    .set_organizational_unit_name('Main Branch')
    .set_registered_address('Your Address, Riyadh, Saudi Arabia')
    .set_invoice_type(True, True)  # Tax and Simplified invoices
    .set_current_zatca_env('sandbox')  # sandbox, simulation, production
    .set_business_category('company'))

# Generate CSR
csr = GenerateCSR.from_request(csr_request).initialize().generate()

# Save CSR for submission to ZATCA
with open('csr.pem', 'w') as f:
    f.write(csr.get_csr_content())

# Save private key (keep secure!)
private_key = csr.get_private_key()
with open('private_key.pem', 'wb') as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

print("CSR generated and saved as 'csr.pem'")
print("Private key saved as 'private_key.pem'")
```

### 3. Certificate Management

```python
from pyzatca import Certificate

# Load certificate (you'll get these from ZATCA)
certificate = Certificate(
    'certificate_plain_text',  # From ZATCA
    'private_key_plain_text'   # Your private key
).set_secret_key('secret_key_text')  # From ZATCA

# Generate authorization header for ZATCA APIs
auth_header = certificate.get_authorization_header()
print(f"Authorization: {auth_header}")

# Get certificate hash
cert_hash = certificate.get_hash()
print(f"Certificate Hash: {cert_hash}")

# Get public key
public_key = certificate.get_plain_public_key()
print(f"Public Key: {public_key}")
```

### 4. Invoice Signing (Advanced)

```python
from pyzatca import Certificate, InvoiceSign

# Your invoice XML (simplified example)
invoice_xml = """
<Invoice>
    <Seller>Your Company</Seller>
    <VATNumber>123456789012345</VATNumber>
    <Amount>100.00</Amount>
    <TaxAmount>15.00</TaxAmount>
    <Date>2025-08-05T07:21:06Z</Date>
</Invoice>
"""

# Load certificate
certificate = Certificate(
    'certificate_from_zatca',
    'your_private_key'
).set_secret_key('secret_key_from_zatca')

# Sign invoice
invoice = InvoiceSign(invoice_xml, certificate).sign()

# Get results
invoice_hash = invoice.get_hash()
signed_invoice = invoice.get_invoice()
qr_code = invoice.get_qr_code()

print(f"Invoice Hash: {invoice_hash}")
print(f"QR Code: {qr_code}")
```

### 5. Arabic Text Support

```python
from pyzatca import GenerateQrCode
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount

# Generate QR code with Arabic text
qr_code = GenerateQrCode.from_array([
    Seller('شركة حدث لتقنية المعلومات'),  # Arabic company name
    TaxNumber('123456789012345'),
    InvoiceDate('2025-08-05T07:21:06Z'),
    InvoiceTotalAmount('100.00'),
    InvoiceTaxAmount('15.00')
]).to_base64()

print(f"Arabic QR Code: {qr_code}")
```

## 🔧 Advanced Usage

### Custom QR Code Options

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

# Custom QR code options
qr_generator.render(
    file_path='custom_qr.png',
    options={
        'box_size': 10,
        'border': 4,
        'fill_color': 'black',
        'back_color': 'white'
    }
)
```

### Error Handling

```python
from pyzatca import GenerateQrCode, CSRRequest
from pyzatca.models.csr_request import CSRValidationException

try:
    # Generate QR code
    qr_code = GenerateQrCode.from_array([
        Seller('Your Company'),
        TaxNumber('123456789012345'),
        InvoiceDate('2025-08-05T07:21:06Z'),
        InvoiceTotalAmount('100.00'),
        InvoiceTaxAmount('15.00')
    ]).to_base64()
    
    print(f"QR Code: {qr_code}")
    
except ValueError as e:
    print(f"QR Code Error: {e}")

try:
    # Create CSR request
    csr_request = (CSRRequest.make()
        .set_uid('123456789012345')
        .set_common_name('Your Company')
        .set_country_name('SA'))
    
except CSRValidationException as e:
    print(f"CSR Validation Error: {e}")
```

## 📊 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pyzatca

# Run specific test
pytest tests/test_generate_qr_code.py -v
```

## 🔍 Debugging

```python
from pyzatca import GenerateQrCode
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount

# Generate TLV string for debugging
tlv_string = GenerateQrCode.from_array([
    Seller('Your Company'),
    TaxNumber('123456789012345'),
    InvoiceDate('2025-08-05T07:21:06Z'),
    InvoiceTotalAmount('100.00'),
    InvoiceTaxAmount('15.00')
]).to_tlv()

print(f"TLV String: {tlv_string}")
```

## 📚 API Reference

### Main Classes

- `GenerateQrCode` - Generate ZATCA-compliant QR codes
- `GenerateCSR` - Generate Certificate Signing Requests
- `CSRRequest` - Model for CSR request data
- `Certificate` - Certificate management and operations
- `InvoiceSign` - Invoice signing and digital signatures

### Tag Classes

- `Seller` - Company name (Tag 1)
- `TaxNumber` - VAT number (Tag 2)
- `InvoiceDate` - Invoice date (Tag 3)
- `InvoiceTotalAmount` - Total amount (Tag 4)
- `InvoiceTaxAmount` - Tax amount (Tag 5)
- `InvoiceHash` - Invoice hash (Tag 5)
- `InvoiceDigitalSignature` - Digital signature (Tag 6)
- `PublicKey` - Public key (Tag 7)
- `CertificateSignature` - Certificate signature (Tag 8)

## 🚨 Important Notes

1. **Keep Private Keys Secure**: Never share your private key
2. **Test in Sandbox**: Always test in ZATCA sandbox first
3. **Validate Data**: Ensure all invoice data is accurate
4. **Handle Errors**: Implement proper error handling
5. **Follow ZATCA Guidelines**: Stay compliant with ZATCA requirements

## 📞 Support

- **GitHub Issues**: Report bugs and request features
- **Documentation**: Check the README for more details
- **Examples**: See the `examples/` directory for working code 