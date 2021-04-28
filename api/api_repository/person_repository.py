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
        person = Person()
        person.id = model.id
        person.email = model.email
        person.first_name = model.first_name
        person.last_name = model.last_name
        person.password = model.password
        person.telephone = model.telephone
        person.date_created = model.date_created
        person.save()

    def update_person(self, person_id, model: UpdatePersonDto):
        try:
            person = Person.objects.get(id=person_id)
            person.first_name = model.first_name
            person.last_name = model.last_name
            person.telephone = model.telephone
            person.date_updated = model.date_updated
        except Person.DoesNotExist as e:
            raise e

    def list_person(self) -> List[ListPersonDto]:
        persons = Person.objects.all()
        results: List[ListPersonDto] = []
        for person in persons:
            item = ListPersonDto()
            item.first_name = person.first_name
            item.last_name = person.last_name
            item.telephone = person.telephone
            item.role = person.role
            results.append(item)
        return results

    def person_details(self, person_id, model: PersonDetailsDto):
        try:
            person = Person.objects.get(id=person_id)
            person.id = model.id
            person.email = model.email
            person.first_name = model.first_name
            person.last_name = model.last_name
            person.telephone = model.telephone
            person.address = model.address
            person.role = model.role
            person.permission = model.permission
            person.date_created = model.date_created
            person.date_updated = model.date_updated
            return person
        except Person.DoesNotExist as e:
            raise e
