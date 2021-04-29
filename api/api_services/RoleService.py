from abc import ABCMeta, abstractmethod
from typing import List

from TMS.api.api_dto.RoleDto import *
from TMS.api.api_repository.RoleRepository import RoleRepository
from TMS.api.models import Role


class RoleManagementService(metaclass=ABCMeta):
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

    @abstractmethod
    def update_role_permissions(self, role_id, model: UpdateRolePermissionDto):
        """Edit the permissions assigned to a role"""
        raise NotImplementedError


class DefaultRoleManagementService(RoleManagementService):
    repository: RoleRepository

    def __init__(self, repository: RoleRepository):
        self.repository = repository

    def create_role(self, model: CreateRoleDto):
        role = self.repository.get(name=model.name)
        if isinstance(role, (RoleDetailsDto,)):
            return False
        else:
            return self.repository.create_role(model=model)

    def update_role(self, role_id, model: UpdateRoleDto):
        result = self.repository.update_role(role_id, model)
        if isinstance(result, (Exception, Role.DoesNotExist)):
            return True
        return False

    def list_role(self) -> List[ListRoleDto]:
        return self.repository.list_role()

    def role_details(self, role_id, model: RoleDetailsDto):
        role = self.repository.get(role_id)
        if isinstance(role, (RoleDetailsDto,)):
            return role

    def update_role_permissions(self, role_id, model: UpdateRolePermissionDto):
        return self.repository.update_role(role_id, model)
