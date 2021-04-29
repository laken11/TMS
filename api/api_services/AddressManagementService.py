from abc import ABCMeta, abstractmethod
from typing import List, Union

from api.api_dto.AddressDto import *
from api.api_repository.AddressRepository import AddressRepository
from api.models import Address


class AddressManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_address(self, model: CreateAddressDto):
        """Create Address"""
        raise NotImplemented

    def list_address(self) -> List[ListAddressDto]:
        """List Address"""
        raise NotImplemented

    def address_details(self, address_id=None, name=None) -> AddressDetailsDto:
        """Address Details"""
        raise NotImplemented

    def edit_address(self, address_id: int, model: EditAddressDto):
        """Edit Address"""
        raise NotImplemented


class DefaultAddressManagementService(AddressManagementService):
    repository: AddressRepository

    def __init__(self, repository: AddressRepository):
        self.repository = repository

    def create_address(self, model: CreateAddressDto):
        try:
            self.repository.address_details(id=model.id)
        except Address.DoesNotExist:
            self.repository.create_address(model)
            return True
        else:
            return False

    def list_address(self) -> List[ListAddressDto]:
        return self.repository.list_address()

    def edit_address(self, address_id: int, model: EditAddressDto):
        return self.repository.edit_address(address_id, model)

    def address_details(self, address_id=None) -> Union[AddressDetailsDto, bool]:
        try:
            return self.repository.address_details(address_id)
        except Address.DoesNotExist:
            return False
