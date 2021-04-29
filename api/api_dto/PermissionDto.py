from datetime import date


class CreatePermissionDto:
    id: str
    name: str
    description: str
    date_created: date


class UpdatePermissionDto:
    name: str
    description: str
    date_updated: date


class ListPermissionDto:
    name: str
    description: str


class PermissionDetailsDto:
    id: str
    name: str
    description: str
    date_created: date
    date_updated: date