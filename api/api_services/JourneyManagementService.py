from abc import ABCMeta, abstractmethod
from api.dto.journey_dto import *
from api.api_repository.JourneyRepository import JourneyRepository
from typing import List, Union
from api.models import Journey


class JourneyManagementService(metaclass=ABCMeta):
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


class DefaultJourneyManagementService(JourneyManagementService):
    repository: JourneyRepository

    def __init__(self, repository: JourneyRepository):
        self.repository = repository

    def create_journey(self, model: CreateJourneyDto):
        try:
            self.repository.get_journey(journey_id=model.id)
        except Journey.DoesNotExist:
            return self.repository.create_journey(model)

    def edit_journey(self, journey_id: int, model: EditJourneyDto):
        return self.repository.edit_journey(journey_id, model)

    def list_journeys(self) -> List[ListJourneyDto]:
        return self.repository.list_journeys()

    def get_journey(self, journey_id: int) -> Union[GetJourneyDto, bool]:
        try:
            return self.repository.get_journey(journey_id)
        except Journey.DoesNotExist:
            return False
