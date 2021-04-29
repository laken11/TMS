from abc import ABCMeta, abstractmethod
from typing import List

from TMS.api.api_dto.AddressDto import *
from TMS.api.models import Address


class AddressRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_address(self, model: CreateAddressDto):
        """Create Address"""
        raise NotImplemented

    @abstractmethod
    def list_address(self) -> List[ListAddressDto]:
        """List Address"""
        raise NotImplemented

    @abstractmethod
    def address_details(self, address_id=None, name=None) -> AddressDetailsDto:
        """Address Details"""
        raise NotImplemented

    @abstractmethod
    def edit_address(self, address_id: int, model: EditAddressDto):
        """Edit Address"""
        raise NotImplemented


class DjangoORMAddressRepository(AddressRepository):
    def create_address(self, model: CreateAddressDto):
        address = Address()
        address.line = model.line
        address.postal_code = model.postal_code
        address.city = model.city
        address.country = model.country
        address.state = model.state
        address.save()

    def list_address(self) -> List[ListAddressDto]:
        address = Address.objects.all()
        result: List[ListAddressDto] = []
        for address in address:
            item = ListAddressDto()
            item.line = address.line
            item.postal_code = address.postal_code
            item.id = address.id
            item.state = address.state
            item.country = address.country
            item.city = address.city
            result.append(item)
        return result

    def edit_address(self, address_id: int, model: EditAddressDto):
        try:
            address = Address.objects.get(id=address_id)
            address.line = model.line
            address.postal_code = model.postal_code
            address.country = model.country
            address.state = model.state
            address.city = model.city
            address.save()
        except Address.DoesNotExist as e:
            return e

    def address_details(self, address_id=None, name=None) -> AddressDetailsDto:
        address = Address()
        try:
            if address_id is not None:
                address = Address.objects.get(id=address_id)
                result = AddressDetailsDto()
                result.line = address.line
                result.postal_code = address.postal_code
                result.country = address.country
                result.state = address.state
                result.city = address.city
                result.id = address.id
                return result
        except Address.DoesNotExist as e:
            return e
