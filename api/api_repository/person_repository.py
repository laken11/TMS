from abc import ABCMeta, abstractmethod
from typing import List

from TMS.api.api_dto.person_dto import *
from TMS.api.models import Person


class PersonRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_person(self, model: CreatePersonDto):
        """Create a person object"""
        raise NotImplementedError

    @abstractmethod
    def update_person(self, person_id, model: UpdatePersonDto):
        """Update a person object"""
        raise NotImplementedError

    @abstractmethod
    def list_person(self) -> List[ListPersonDto]:
        """List all person objects"""
        raise NotImplementedError

    @abstractmethod
    def person_details(self, person_id, model: PersonDetailsDto):
        """Details of a person object"""
        raise NotImplementedError


class DjangoORMPersonRepository(PersonRepository):
    def create_person(self, model: CreatePersonDto):
        pass

    def update_person(self, person_id, model: UpdatePersonDto):
        pass

    def list_person(self) -> List[ListPersonDto]:
        pass

    def person_details(self, person_id, model: PersonDetailsDto):
        pass