"""
CSR Request model for ZATCA.
"""

from typing import Dict, Any


class CSRValidationException(Exception):
    """Exception raised for CSR validation errors."""
    pass


class CSRRequest:
    """
    Certificate Signing Request (CSR) model for ZATCA.
    
    This class handles the creation and validation of CSR requests
    for ZATCA e-invoicing integration.
    """
    
    SANDBOX = 'sandbox'
    SIMULATION = 'simulation'
    PRODUCTION = 'production'
    
    def __init__(self):
        """Initialize a new CSR request."""
        self.serial_number = None
        self.invoice_type = '1100'  # Default: Tax and Simplified invoices
        self.common_name = None
        self.organization_name = None
        self.organizational_unit_name = None
        self.country_name = None
        self.uid = None
        self.registered_address = None
        self.business_category = 'company'
        self.current_env = 'sandbox'
    
    @classmethod
    def make(cls) -> 'CSRRequest':
        """Create a new CSR request instance."""
        return cls()
    
    def set_common_name(self, common_name: str) -> 'CSRRequest':
        """Set the common name."""
        self.common_name = common_name
        return self
    
    def set_organization_name(self, organization_name: str) -> 'CSRRequest':
        """Set the organization name."""
        self.organization_name = organization_name
        return self
    
    def set_organizational_unit_name(self, organizational_unit_name: str) -> 'CSRRequest':
        """Set the organizational unit name."""
        if (self.uid and 
            len(self.uid) > 10 and 
            self.uid[10] == '1' and 
            len(organizational_unit_name) != 10):
            raise CSRValidationException(
                'The Organization Unit Name Must Match this '
                '(If 11th digit of Organization Identifier(UID) = 1 then needs to be 10 digit number)'
            )
        
        self.organizational_unit_name = organizational_unit_name
        return self
    
    def set_country_name(self, country_name: str) -> 'CSRRequest':
        """Set the country name."""
        if len(country_name) != 2:
            raise CSRValidationException('The Country name must be Two chars only')
        
        self.country_name = country_name
        return self
    
    def set_uid(self, uid: str) -> 'CSRRequest':
        """Set the UID (Organization Identifier)."""
        if (len(uid) != 15 or 
            not uid.startswith('3') or 
            not uid.endswith('3')):
            raise CSRValidationException(
                'The Organization Identifier must be 15 digits, starting and ending with 3'
            )
        
        self.uid = uid
        return self
    
    def set_registered_address(self, registered_address: str) -> 'CSRRequest':
        """Set the registered address."""
        self.registered_address = registered_address
        return self
    
    def set_business_category(self, business_category: str) -> 'CSRRequest':
        """Set the business category."""
        self.business_category = business_category
        return self
    
    def set_serial_number(self, solution_name: str, version: str, serial_number: str) -> 'CSRRequest':
        """Set the serial number."""
        self.serial_number = f"1-{solution_name}|2-{version}|3-{serial_number}"
        return self
    
    def set_invoice_type(self, tax_invoice: bool, simplified: bool) -> 'CSRRequest':
        """Set the invoice type."""
        self.invoice_type = f"{int(tax_invoice)}{int(simplified)}00"
        return self
    
    def set_current_zatca_env(self, current_env: str) -> 'CSRRequest':
        """Set the current ZATCA environment."""
        self.current_env = current_env
        return self
    
    def is_sandbox_env(self) -> bool:
        """Check if the environment is sandbox."""
        return self.current_env == self.SANDBOX
    
    def is_simulation_env(self) -> bool:
        """Check if the environment is simulation."""
        return self.current_env == self.SIMULATION
    
    def is_production(self) -> bool:
        """Check if the environment is production."""
        return self.current_env == self.PRODUCTION
    
    def to_array(self) -> Dict[str, Any]:
        """Convert the CSR request to an array format."""
        return {
            'dn': {
                "CN": self.get_common_name(),
                "organizationName": self.get_organization_name(),
                "organizationalUnitName": self.get_organizational_unit_name(),
                "C": self.get_country()
            },
            'subject': {
                "SN": self.get_serial_number(),
                "UID": self.get_uid(),
                "title": self.get_invoice_type(),
                "registeredAddress": self.get_registered_address(),
                "businessCategory": self.get_business_category()
            }
        }
    
    def get_serial_number(self) -> str:
        """Get the serial number."""
        return self.serial_number or ""
    
    def get_common_name(self) -> str:
        """Get the common name."""
        return self.common_name or ""
    
    def get_organization_name(self) -> str:
        """Get the organization name."""
        return self.organization_name or ""
    
    def get_organizational_unit_name(self) -> str:
        """Get the organizational unit name."""
        return self.organizational_unit_name or ""
    
    def get_uid(self) -> str:
        """Get the UID."""
        return self.uid or ""
    
    def get_invoice_type(self) -> str:
        """Get the invoice type."""
        return self.invoice_type
    
    def get_registered_address(self) -> str:
        """Get the registered address."""
        return self.registered_address or ""
    
    def get_business_category(self) -> str:
        """Get the business category."""
        return self.business_category
    
    def get_country(self) -> str:
        """Get the country name."""
        return self.country_name or "" 