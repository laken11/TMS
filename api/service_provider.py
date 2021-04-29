from typing import Callable

from dependency_injector import containers, providers

from TMS.api.api_repository.PersonRepository import *
from TMS.api.api_repository.PermissionRepository import *
from TMS.api.api_repository.RoleRepository import *


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    person_repository: Callable[[], PersonRepository] = providers.Factory(
        DjangoORMPersonRepository
    )

    permission_repository: Callable[[], PermissionRepository] = providers.Factory(
        DjangoORMPermissionRepository
    )

    role_repository: Callable[[], RoleRepository] = providers.Factory(
        DjangoORMRoleRepository
    )

service_provider = Container()