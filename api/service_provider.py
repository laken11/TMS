from typing import Callable

from dependency_injector import containers, providers

from TMS.api.api_repository.PersonRepository import *
from TMS.api.api_repository.PermissionRepository import *
from TMS.api.api_repository.RoleRepository import *
from TMS.api.api_repository.AddressRepository import *
from TMS.api.api_repository.DestinationRepository import *


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

    address_repository: Callable[[], AddressRepository] = providers.Factory(
        DjangoORMAddressRepository
    )

    destination_repository: Callable[[], DestinationRepository] = providers.Factory(
        DjangoORMDestinationRepository
    )

service_provider = Container()