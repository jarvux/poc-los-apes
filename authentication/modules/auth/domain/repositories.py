from abc import ABC
from authentication.seedwork.domain.repositories import Repository


class RepositoryUsers(Repository, ABC):
    ...
