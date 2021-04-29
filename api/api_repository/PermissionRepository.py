from abc import abstractmethod, ABCMeta
from typing import List

from api.api_dto.PermissionDto import *
from api.models import Permission


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
        permissions = Permission.objects.all()
        results: List[ListPermissionDto] = []
        for permission in permissions:
            item = ListPermissionDto()
            item.name = permission.name
            item.description = permission.description
            results.append(item)
        return results

    def permission_details(self, permission_id, model: PermissionDetailsDto):
        try:
            permission = Permission.objects.get(id=permission_id)
            result = PermissionDetailsDto()
            result.id = permission.id
            result.name = permission.name
            result.description = permission.description
            result.date_created = permission.date_created
            result.date_updated = permission.date_updated
            return result
        except Permission.DoesNotExist as e:
            return e
