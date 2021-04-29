from abc import ABCMeta, abstractmethod
from typing import List, Union

from api.Dto.DestinationDto import *
from api.Repository.DestinationRepository import DestinationRepository
from api.models import Address, Destination


class DestinationManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_destination(self, model: CreateDestinationDto):
        """Create Destination"""
        raise NotImplemented

    @abstractmethod
    def list_destination(self) -> List[ListDestinationDto]:
        """List Destination"""
        raise NotImplemented

    @abstractmethod
    def destination_details(self, destination_id=None, name=None) -> DestinationDetailsDto:
        """Destination Details"""
        raise NotImplemented

    @abstractmethod
    def edit_destination(self, destination_id: int, model: EditDestination):
        """Edit Destination"""
        raise NotImplemented


class DefaultDestinationManagementService(DestinationManagementService):
    repository: DestinationRepository

    def __init__(self, repository: DestinationRepository):
        self.repository = repository

    def create_destination(self, model: CreateDestinationDto):
        try:
            self.repository.destination_details(id=model.id)
        except Destination.DoesNotExist:
            self.repository.create_destination(model)
            return True
        else:
            return False

    def list_destination(self) -> List[ListDestinationDto]:
        return self.repository.list_destination()

    def edit_destination(self, destination_id: int, model: EditDestination):
        return self.repository.edit_destination(destination_id, model)

    def destination_details(self, destination_id=None) -> Union[DestinationDetailsDto, bool]:
        try:
            return self.repository.destination_details(destination_id)
        except Destination.DoesNotExist:
            return False
