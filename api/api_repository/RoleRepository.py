from abc import ABCMeta, abstractmethod
from typing import List

from TMS.api.api_dto.RoleDto import *
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

    @abstractmethod
    def update_role_permissions(self, role_id, model: UpdateRolePermissionDto):
        """Edit the permissions assigned to a role"""
        raise NotImplementedError


class DjangoORMRoleRepository(RoleRepository):
    def create_role(self, model: CreateRoleDto):
        role = Role()
        role.id = model.id
        role.name = model.name
        role.description = model.description
        role.date_created = model.date_created
        role.permission = model.permission
        role.save()

    def update_role(self, role_id, model: UpdateRoleDto):
        try:
            role = Role.objects.get(id=role_id)
            role.name = model.name
            role.description = model.description
            role.date_updated = model.date_updated
            role.save()
        except Role.DoesNotExist as e:
            raise e

    def list_role(self) -> List[ListRoleDto]:
        roles = Role.objects.all()
        results: List[ListRoleDto] = []
        for role in roles:
            item = ListRoleDto()
            item.name = role.name
            item.description = role.description
            item.permission = role.permission
            results.append(item)
        return results

    def role_details(self, role_id, model: RoleDetailsDto):
        try:
            role = Role.objects.get(id=role_id)
            result = RoleDetailsDto()
            result.id = role.id
            result.name = role.name
            result.description = role.description
            result.permission = role.permission
            result.date_created = role.date_created
            result.date_updated = role.date_updated
            return result
        except Role.DoesNotExist as e:
            return e

    def update_role_permissions(self, role_id, model: UpdateRolePermissionDto):
        try:
            role = Role.objects.get(id=role_id)
            role.permission = model.permission_id
            role.date_updated = model.date_updated
            role.save()
        except Role.DoesNotExist as e:
            raise e