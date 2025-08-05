"""
Tests for GenerateQrCode class.
"""

import pytest
from pyzatca import GenerateQrCode, Tag
from pyzatca.tags import Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount


class TestGenerateQrCode:
    """Test cases for GenerateQrCode class."""
    
    def test_should_generate_qr_code(self):
        """Test basic QR code generation."""
        generated_string = GenerateQrCode.from_array([
            Tag(1, 'Salla'),
            Tag(2, '1234567891'),
            Tag(3, '2021-07-12T14:25:09Z'),
            Tag(4, '100.00'),
            Tag(5, '15.00')
        ]).to_base64()
        
        expected = 'AQVTYWxsYQIKMTIzNDU2Nzg5MQMUMjAyMS0wNy0xMlQxNDoyNTowOVoEBjEwMC4wMAUFMTUuMDA='
        assert generated_string == expected
    
    def test_should_generate_qr_code_as_arabic(self):
        """Test QR code generation with Arabic text."""
        generated_string = GenerateQrCode.from_array([
            Tag(1, 'سلة'),
            Tag(2, '1234567891'),
            Tag(3, '2021-07-12T14:25:09Z'),
            Tag(4, '100.00'),
            Tag(5, '15.00')
        ]).to_base64()
        
        expected = 'AQbYs9mE2KkCCjEyMzQ1Njc4OTEDFDIwMjEtMDctMTJUMTQ6MjU6MDlaBAYxMDAuMDAFBTE1LjAw'
        assert generated_string == expected
    
    def test_should_generate_qr_code_from_tags_classes(self):
        """Test QR code generation using tag classes."""
        generated_string = GenerateQrCode.from_array([
            Seller('Salla'),
            TaxNumber('1234567891'),
            InvoiceDate('2021-07-12T14:25:09Z'),
            InvoiceTotalAmount('100.00'),
            InvoiceTaxAmount('15.00')
        ]).to_base64()
        
        expected = 'AQVTYWxsYQIKMTIzNDU2Nzg5MQMUMjAyMS0wNy0xMlQxNDoyNTowOVoEBjEwMC4wMAUFMTUuMDA='
        assert generated_string == expected
    
    def test_should_generate_qr_code_display_as_image_data(self):
        """Test QR code image generation."""
        generated_string = GenerateQrCode.from_array([
            Seller('Salla'),
            TaxNumber('1234567891'),
            InvoiceDate('2021-07-12T14:25:09Z'),
            InvoiceTotalAmount('100.00'),
            InvoiceTaxAmount('15.00')
        ]).render()
        
        # Should start with data:image/png;base64,
        assert generated_string.startswith('data:image/png;base64,')
    
    def test_should_throw_exception_with_wrong_data(self):
        """Test exception handling with invalid data."""
        with pytest.raises(ValueError, match='malformed data structure'):
            GenerateQrCode.from_array([None]).to_base64()
    
    def test_should_generate_tlv_string(self):
        """Test TLV string generation."""
        tlv_string = GenerateQrCode.from_array([
            Seller('Salla'),
            TaxNumber('1234567891'),
            InvoiceDate('2021-07-12T14:25:09Z'),
            InvoiceTotalAmount('100.00'),
            InvoiceTaxAmount('15.00')
        ]).to_tlv()
        
        # Should be a non-empty string
        assert isinstance(tlv_string, str)
        assert len(tlv_string) > 0 