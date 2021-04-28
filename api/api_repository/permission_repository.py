from abc import abstractmethod, ABCMeta
from typing import List

from TMS.api.api_dto.permission_dto import *
from TMS.api.models import Permission


class PermissionRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_permission(self, model: CreatePermissionDto):
        """Create a permission object"""
        raise NotImplementedError

    @abstractmethod
    def update_permission(self, permission_id: str, model: UpdatePermissionDto):
        """Update a permission object"""
        raise NotImplementedError

    @abstractmethod
    def list_permission(self) -> List[ListPermissionDto]:
        """List all Permission objects"""
        raise NotImplementedError

    @abstractmethod
    def permission_details(self, permission_id, model: PermissionDetailsDto):
        """Details of a particular permission object"""
        raise NotImplementedError


class DjangoORMPermissionRepository(PermissionRepository):
    def create_permission(self, model: CreatePermissionDto):
        permission = Permission()
        permission.id = model.id
        permission.name = model.name
        permission.description = model.description
        permission.date_created = model.date_created
        permission.save()

    def update_permission(self, permission_id: str, model: UpdatePermissionDto):
        try:
            permission = Permission.objects.get(id=permission_id)
            permission.name = model.name
            permission.description = model.description
            permission.save()
        except Permission.DoesNotExist as e:
            return e

    def list_permission(self) -> List[ListPermissionDto]:
        pass

    def permission_details(self, permission_id, model: PermissionDetailsDto):
        pass
