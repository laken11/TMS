from abc import ABCMeta, abstractmethod
from typing import List

from TMS.api.api_dto.role_dto import *
from TMS.api.models import Role


class RoleRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_role(self, model: CreateRoleDto):
        """Create a role object"""
        raise NotImplementedError

    @abstractmethod
    def update_role(self, role_id, model: UpdateRoleDto):
        """Update a role object"""
        raise NotImplementedError

    @abstractmethod
    def list_role(self) -> List[ListRoleDto]:
        """List all role objects"""
        raise NotImplementedError

    @abstractmethod
    def role_details(self, role_id, model: RoleDetailsDto):
        """Details of a role object"""
        raise NotImplementedError


class DjangoORMRoleRepository(RoleRepository):
    def create_role(self, model: CreateRoleDto):
        pass

    def update_role(self, role_id, model: UpdateRoleDto):
        pass

    def list_role(self) -> List[ListRoleDto]:
        pass

    def role_details(self, role_id, model: RoleDetailsDto):
        pass