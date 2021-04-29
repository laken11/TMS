from abc import ABCMeta, abstractmethod
from typing import List

from TMS.api.api_dto.person_dto import *
from TMS.api.api_repository.person_repository import PersonRepository


class PersonManagementService(metaclass=ABCMeta):
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

    @abstractmethod
    def update_person_role(self, person_id, model: UpdatePersonRoleDto):
        """Updating a person role"""
        raise NotImplementedError


class DefaultPersonManagementService(PersonManagementService):
    repository: PersonRepository

    def __init__(self, repository: PersonRepository):
        self.repository = repository

    def create_person(self, model: CreatePersonDto):
        return self.repository.create_person(model=model)

    def update_person(self, person_id, model: UpdatePersonDto):
        return self.update_person(person_id=person_id, model=model)

    def list_person(self) -> List[ListPersonDto]:
        return self.repository.list_person()

    def person_details(self, person_id, model: PersonDetailsDto):
        return self.repository.person_details(person_id=person_id, model=model)

    def update_person_role(self, person_id, model: UpdatePersonRoleDto):
        return self.repository.update_person_role(person_id=person_id, model=model)