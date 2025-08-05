"""
Tests for CSRRequest class.
"""

import pytest
from pyzatca.models.csr_request import CSRRequest, CSRValidationException


class TestCSRRequest:
    """Test cases for CSRRequest class."""
    
    def test_should_create_csr_request(self):
        """Test basic CSR request creation."""
        request = CSRRequest.make()
        assert isinstance(request, CSRRequest)
    
    def test_should_set_common_name(self):
        """Test setting common name."""
        request = CSRRequest.make().set_common_name('Test Company')
        assert request.get_common_name() == 'Test Company'
    
    def test_should_set_organization_name(self):
        """Test setting organization name."""
        request = CSRRequest.make().set_organization_name('Test Organization')
        assert request.get_organization_name() == 'Test Organization'
    
    def test_should_set_country_name(self):
        """Test setting country name."""
        request = CSRRequest.make().set_country_name('SA')
        assert request.get_country() == 'SA'
    
    def test_should_throw_exception_for_invalid_country_name(self):
        """Test exception for invalid country name."""
        with pytest.raises(CSRValidationException, match='The Country name must be Two chars only'):
            CSRRequest.make().set_country_name('SAU')
    
    def test_should_set_uid(self):
        """Test setting UID."""
        request = CSRRequest.make().set_uid('310461435700003')
        assert request.get_uid() == '310461435700003'
    
    def test_should_throw_exception_for_invalid_uid(self):
        """Test exception for invalid UID."""
        with pytest.raises(CSRValidationException, match='The Organization Identifier must be 15 digits'):
            CSRRequest.make().set_uid('123456789')
    
    def test_should_set_serial_number(self):
        """Test setting serial number."""
        request = CSRRequest.make().set_serial_number('MyApp', '1.0', '123456')
        assert request.get_serial_number() == '1-MyApp|2-1.0|3-123456'
    
    def test_should_set_invoice_type(self):
        """Test setting invoice type."""
        request = CSRRequest.make().set_invoice_type(True, True)
        assert request.get_invoice_type() == '1100'
    
    def test_should_set_current_zatca_env(self):
        """Test setting ZATCA environment."""
        request = CSRRequest.make().set_current_zatca_env('sandbox')
        assert request.is_sandbox_env() is True
        assert request.is_simulation_env() is False
        assert request.is_production() is False
    
    def test_should_convert_to_array(self):
        """Test conversion to array format."""
        request = (CSRRequest.make()
                  .set_common_name('Test Company')
                  .set_organization_name('Test Organization')
                  .set_country_name('SA')
                  .set_uid('310461435700003'))
        
        array_data = request.to_array()
        
        assert 'dn' in array_data
        assert 'subject' in array_data
        assert array_data['dn']['CN'] == 'Test Company'
        assert array_data['dn']['organizationName'] == 'Test Organization'
        assert array_data['dn']['C'] == 'SA'
        assert array_data['subject']['UID'] == '310461435700003' 