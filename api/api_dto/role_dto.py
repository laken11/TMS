from datetime import date


class CreateRoleDto:
    id: str
    name: str
    description: str
    date_created: date
    permission: str


class UpdateRoleDto:
    name: str
    description: str
    date_updated: date
    permission: str


class ListRoleDto:
    name: str
    description: str
    permission: str


class RoleDetailsDto:
    id: str
    name: str
    description: str
    permission: str
    date_created: date
    date_updated: date
