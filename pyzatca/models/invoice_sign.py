"""
Invoice Sign model for ZATCA.
"""

import hashlib
import base64
from typing import List
from .invoice import Invoice
from ..helpers.certificate import Certificate
from ..tags.invoice_hash import InvoiceHash
from ..tags.invoice_digital_signature import InvoiceDigitalSignature
from ..tags.public_key import PublicKey
from ..tags.certificate_signature import CertificateSignature
from ..generate_qr_code import GenerateQrCode


class InvoiceSign:
    """
    Invoice signing for ZATCA e-invoicing.
    
    This class handles the signing of invoices and generation of QR codes.
    """
    
    def __init__(self, xml_invoice: str, certificate: Certificate):
        """
        Initialize the invoice signer.
        
        Args:
            xml_invoice (str): The invoice XML content
            certificate (Certificate): The certificate for signing
        """
        self.xml_invoice = xml_invoice
        self.certificate = certificate
        self.invoice = Invoice(xml_invoice)
    
    def sign(self) -> 'InvoiceSign':
        """
        Sign the invoice.
        
        Returns:
            InvoiceSign: Self for method chaining
        """
        # In a real implementation, this would involve XML signing
        # For now, we'll create a basic implementation
        return self
    
    def get_hash(self) -> str:
        """
        Get the invoice hash.
        
        Returns:
            str: The invoice hash
        """
        # Generate hash of the XML content
        return base64.b64encode(
            hashlib.sha256(self.xml_invoice.encode('utf-8')).digest()
        ).decode('ascii')
    
    def get_invoice(self) -> str:
        """
        Get the signed invoice XML.
        
        Returns:
            str: The signed invoice XML
        """
        # In a real implementation, this would return the signed XML
        # For now, return the original XML
        return self.xml_invoice
    
    def get_qr_code(self) -> str:
        """
        Get the QR code as base64.
        
        Returns:
            str: The QR code as base64 encoded string
        """
        # Create tags for QR code
        tags = [
            InvoiceHash(self.get_hash()),
            InvoiceDigitalSignature("signature_placeholder"),  # Would be actual signature
            PublicKey(self.certificate.get_plain_public_key()),
            CertificateSignature(self.certificate.get_certificate_signature())
        ]
        
        return GenerateQrCode.from_array(tags).to_base64() 