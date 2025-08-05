"""
Generate CSR for ZATCA e-invoicing.
"""

import tempfile
import os
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from .models.csr_request import CSRRequest
from .models.csr import CSR


class GenerateCSR:
    """
    Generate Certificate Signing Request (CSR) for ZATCA e-invoicing.
    
    This class handles the generation of CSR requests for ZATCA integration.
    """
    
    def __init__(self, csr_request: CSRRequest):
        """
        Initialize the CSR generator.
        
        Args:
            csr_request (CSRRequest): The CSR request data
        """
        self.csr_request = csr_request
        self.data = csr_request.to_array()
    
    @classmethod
    def from_request(cls, csr_request: CSRRequest) -> 'GenerateCSR':
        """
        Create a CSR generator from a request.
        
        Args:
            csr_request (CSRRequest): The CSR request
            
        Returns:
            GenerateCSR: A new GenerateCSR instance
        """
        return cls(csr_request)
    
    def initialize(self) -> 'GenerateCSR':
        """
        Initialize the CSR generator.
        
        Returns:
            GenerateCSR: Self for method chaining
        """
        # In Python, we don't need to create temp config files like in PHP
        # The cryptography library handles this internally
        return self
    
    def generate(self) -> CSR:
        """
        Generate the CSR.
        
        Returns:
            CSR: The generated CSR with content and private key
            
        Raises:
            RuntimeError: If CSR generation fails
        """
        try:
            # Generate private key
            private_key = ec.generate_private_key(
                ec.SECP256K1()
            )
            
            # Create subject name
            subject = x509.Name([
                x509.NameAttribute(NameOID.COMMON_NAME, self.data['dn']['CN']),
                x509.NameAttribute(NameOID.ORGANIZATION_NAME, self.data['dn']['organizationName']),
                x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, self.data['dn']['organizationalUnitName']),
                x509.NameAttribute(NameOID.COUNTRY_NAME, self.data['dn']['C']),
            ])
            
            # Create CSR
            csr = x509.CertificateSigningRequestBuilder().subject_name(
                subject
            ).sign(private_key, hashes.SHA256())
            
            # Export CSR to PEM format
            csr_pem = csr.public_bytes(serialization.Encoding.PEM)
            csr_content = csr_pem.decode('utf-8')
            
            return CSR(csr_content, private_key)
            
        except Exception as e:
            raise RuntimeError(f'Error Generating New Certificate Signing Request: {str(e)}') 