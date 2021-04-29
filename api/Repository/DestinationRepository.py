from abc import ABCMeta, abstractmethod
from typing import List

from api.Dto.DestinationDto import *
from api.models import Destination


class DestinationRepository(metaclass=ABCMeta):
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


class DjangoORMDestinationRepository(DestinationRepository):
    def create_destination(self, model: CreateDestinationDto):
        destination = Destination()
        destination.location = model.location
        destination.description = model.description
        destination.journey = model.journey
        destination.save()

    def list_destination(self) -> List[ListDestinationDto]:
        destinations = Destination.objects.all()
        result: List[ListDestinationDto] = []
        for destination in destinations:
            item = ListDestinationDto()
            item.location = destination.location
            item.journey = destination.journey
            item.id = destination.id
            item.description = destination.description
            result.append(item)
        return result

    def edit_destination(self, destination_id: int, model: EditDestination):
        try:
            destination = Destination.objects.get(id=destination_id)
            destination.location = model.location
            destination.journey = model.journey
            destination.description = model.description
            destination.save()
        except Destination.DoesNotExist as e:
            return e

    def destination_details(self, destination_id=None, name=None) -> DestinationDetailsDto:
        destination = Destination()
        try:
            if destination_id is not None:
                destination = Destination.objects.get(id=destination_id)
                result = DestinationDetailsDto()
                result.location = destination.location
                result.journey = destination.journey
                result.description = destination.description
                result.id = destination.id
                return result
        except Destination.DoesNotExist as e:
            return e
