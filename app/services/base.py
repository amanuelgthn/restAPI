from typing import Callable


class BaseCRMService:
    def __init__(self, client_factory: Callable):
        self.client = client_factory()
