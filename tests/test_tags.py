"""
Tests for Tag classes.
"""

import pytest
from pyzatca.tags import Tag, Seller, TaxNumber, InvoiceDate, InvoiceTotalAmount, InvoiceTaxAmount


class TestTag:
    """Test cases for Tag class."""
    
    def test_should_create_tag(self):
        """Test basic tag creation."""
        tag = Tag(1, 'test_value')
        assert tag.get_tag() == 1
        assert tag.get_value() == 'test_value'
        assert tag.get_length() == 10  # 'test_value' is 10 bytes in UTF-8
    
    def test_should_convert_to_string(self):
        """Test tag to string conversion."""
        tag = Tag(1, 'test')
        tag_string = str(tag)
        assert isinstance(tag_string, str)
        assert len(tag_string) > 0
    
    def test_should_handle_arabic_text(self):
        """Test tag with Arabic text."""
        tag = Tag(1, 'سلة')
        assert tag.get_length() == 6  # Arabic text is 6 bytes in UTF-8
    
    def test_should_handle_numeric_values(self):
        """Test tag with numeric values."""
        tag = Tag(1, 123)
        assert tag.get_value() == '123'


class TestSeller:
    """Test cases for Seller tag."""
    
    def test_should_create_seller_tag(self):
        """Test seller tag creation."""
        seller = Seller('Test Company')
        assert seller.get_tag() == 1
        assert seller.get_value() == 'Test Company'


class TestTaxNumber:
    """Test cases for TaxNumber tag."""
    
    def test_should_create_tax_number_tag(self):
        """Test tax number tag creation."""
        tax_number = TaxNumber('1234567891')
        assert tax_number.get_tag() == 2
        assert tax_number.get_value() == '1234567891'


class TestInvoiceDate:
    """Test cases for InvoiceDate tag."""
    
    def test_should_create_invoice_date_tag(self):
        """Test invoice date tag creation."""
        invoice_date = InvoiceDate('2021-07-12T14:25:09Z')
        assert invoice_date.get_tag() == 3
        assert invoice_date.get_value() == '2021-07-12T14:25:09Z'


class TestInvoiceTotalAmount:
    """Test cases for InvoiceTotalAmount tag."""
    
    def test_should_create_invoice_total_amount_tag(self):
        """Test invoice total amount tag creation."""
        total_amount = InvoiceTotalAmount('100.00')
        assert total_amount.get_tag() == 4
        assert total_amount.get_value() == '100.00'


class TestInvoiceTaxAmount:
    """Test cases for InvoiceTaxAmount tag."""
    
    def test_should_create_invoice_tax_amount_tag(self):
        """Test invoice tax amount tag creation."""
        tax_amount = InvoiceTaxAmount('15.00')
        assert tax_amount.get_tag() == 5
        assert tax_amount.get_value() == '15.00' 