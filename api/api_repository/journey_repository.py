from abc import ABCMeta, abstractmethod
from api.dto.journey_dto import *
from api.models import Vehicle, Journey
from typing import List, Union


class JourneyRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_journey(self, model: CreateJourneyDto):
        """Create Journey Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_journey(self, journey_id: int, model: EditJourneyDto):
        """Edit Journey Object"""
        raise NotImplementedError

    @abstractmethod
    def list_journeys(self) -> List[ListJourneyDto]:
        """List Journey Objects"""
        raise NotImplementedError

    @abstractmethod
    def get_journey(self, journey_id: int) -> Union[GetJourneyDto, bool]:
        """Get Journey Object"""
        raise NotImplementedError


class DjangoORMJourneyRepository(JourneyRepository):
    def create_journey(self, model: CreateJourneyDto):
        journey = Journey()
        journey.id = model.id
        journey.vehicle_id = model.vehicle_id
        journey.name = model.name
        journey.description = model.description
        journey.price = model.price
        journey.save()

    def edit_journey(self, journey_id: int, model: EditJourneyDto):
        journey = Journey.objects.get(id=journey_id)
        journey.name = model.name
        journey.description = model.description
        journey.price = model.price
        journey.vehicle = model.vehicle_id
        journey.save()

    def list_journeys(self) -> List[ListJourneyDto]:
        journeys = Journey.objects.all()
        result: List[ListJourneyDto] = []
        for journey in journeys:
            item = ListJourneyDto()
            item.id = journey.id
            item.vehicle_id = journey.vehicle_id
            item.name = journey.name
            item.description = journey.description
            result.append(item)
        return result

    def get_journey(self, journey_id: int) -> Union[GetJourneyDto, bool]:
        try:
            journey = Journey.objects.get(id=journey_id)
            item = GetJourneyDto()
            item.id = journey.id
            item.vehicle_id = journey.vehicle_id
            item.name = journey.name
            item.description = journey.description
            item.price = journey.price
            return item
        except Journey.DoesNotExist as e:
            return e
