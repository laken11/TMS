from abc import ABCMeta, abstractmethod
from typing import List

from TMS.api.api_dto.permission_dto import *
from TMS.api.api_repository.permission_repository import PermissionRepository


class PermissionManagementService(metaclass=ABCMeta):
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


class DefaultPermissionManagementService(PermissionManagementService):
    repository: PermissionRepository

    def __init__(self, repository: PermissionRepository):
        self.repository = repository

    def create_permission(self, model: CreatePermissionDto):
        return self.repository.create_permission(model=model)

    def update_permission(self, permission_id: str, model: UpdatePermissionDto):
        return self.repository.update_permission(permission_id=permission_id, model=model)

    def list_permission(self) -> List[ListPermissionDto]:
        return self.repository.list_permission()

    def permission_details(self, permission_id, model: PermissionDetailsDto):
        return self.repository.permission_details(permission_id=permission_id, model=model)