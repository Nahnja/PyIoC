from functools import partial
from types import MethodType

class IoCList(list):
    def __getitem__(self, cls):
        return sorted(
            [item for item in self if cls in item.mro()],
            key=lambda item: item.mro().index(cls)
        )[0]

    def inject_dependency(self, **kwargs):
        def decorator(fun):
            keywords = dict([(name, self[cls]()) for name, cls in kwargs.items()])
            # make this work with methods not just plain functions
            # -> partial don't have __get__, functions do, so wrap the partial in a function
            def method(*args, **kwargs):
                return partial(fun, **keywords)(*args, **kwargs)
            return method
        return decorator
