"""
Certificate helper for ZATCA.
"""

import base64
import hashlib
from cryptography import x509
from cryptography.hazmat.primitives import serialization


class Certificate:
    """
    Certificate helper for ZATCA e-invoicing.
    
    This class handles certificate operations including loading,
    validation, and generating authorization headers.
    """
    
    def __init__(self, certificate: str, private_key: str):
        """
        Initialize the certificate helper.
        
        Args:
            certificate (str): The certificate in PEM format
            private_key (str): The private key in PEM format
        """
        self.plain_certificate = certificate
        self.certificate = x509.load_pem_x509_certificate(
            certificate.encode('utf-8')
        )
        self.private_key = serialization.load_pem_private_key(
            private_key.encode('utf-8'),
            password=None
        )
        self.secret_key = None
    
    def set_secret_key(self, secret_key: str) -> 'Certificate':
        """
        Set the secret key for authorization.
        
        Args:
            secret_key (str): The secret key
            
        Returns:
            Certificate: Self for method chaining
        """
        self.secret_key = secret_key
        return self
    
    def get_private_key(self):
        """Get the private key object."""
        return self.private_key
    
    def get_plain_certificate(self) -> str:
        """Get the plain certificate text."""
        return self.plain_certificate
    
    def get_certificate(self) -> x509.Certificate:
        """Get the certificate object."""
        return self.certificate
    
    def get_authorization_header(self) -> str:
        """
        Generate authorization bearer token.
        
        Returns:
            str: The authorization header value
        """
        if not self.secret_key:
            raise ValueError("Secret key must be set before generating authorization header")
        
        cert_b64 = base64.b64encode(self.plain_certificate.encode('utf-8')).decode('ascii')
        return f'Basic {base64.b64encode(f"{cert_b64}:{self.secret_key}".encode("utf-8")).decode("ascii")}'
    
    def get_hash(self) -> str:
        """
        Generate a hash for the certificate.
        
        Returns:
            str: Base64 encoded SHA256 hash
        """
        return base64.b64encode(
            hashlib.sha256(self.plain_certificate.encode('utf-8')).digest()
        ).decode('ascii')
    
    def get_plain_public_key(self) -> str:
        """
        Get public key as plain base64 text.
        
        Returns:
            str: The public key in base64 format
        """
        public_key = self.certificate.public_key()
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        # Remove PEM headers and newlines
        return public_pem.decode('utf-8').replace(
            '-----BEGIN PUBLIC KEY-----\n', ''
        ).replace(
            '\n-----END PUBLIC KEY-----\n', ''
        ).replace('\n', '')
    
    def get_secret_key(self) -> str:
        """
        Get the secret key.
        
        Returns:
            str: The secret key
        """
        return self.secret_key
    
    def get_certificate_signature(self) -> str:
        """
        Get the signature of certificate.
        
        Returns:
            str: The certificate signature
        """
        # Get the signature from the certificate
        signature = self.certificate.signature
        # Remove the first byte as mentioned in the PHP version
        return signature[1:].hex()
    
    def get_formatted_issuer_dn(self) -> str:
        """
        Get the formatted issuer DN.
        
        Returns:
            str: The formatted issuer distinguished name
        """
        issuer = self.certificate.issuer
        # Convert to string format similar to PHP
        return str(issuer) 