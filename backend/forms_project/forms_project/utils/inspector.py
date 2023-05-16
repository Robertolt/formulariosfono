
import importlib
import inspect
import pkgutil
from typing import List, Type

class Inspector:
    @staticmethod
    def get_classes(package_name: str, base_class: Type = object) -> List[Type]:
        package = importlib.import_module(package_name)
        classes = []
        for _, module_name, _ in pkgutil.iter_modules(package.__path__):
            full_module_name = f"{package.__name__}.{module_name}"
            module = importlib.import_module(full_module_name)
            for _, obj in inspect.getmembers(module):
                if inspect.isclass(obj) \
                    and issubclass(obj, base_class) \
                    and (obj not in classes):
                    classes.append(obj)
        return classes

