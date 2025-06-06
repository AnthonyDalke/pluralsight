from importlib import import_module
from inspect import getmembers, isclass, isabstract
from .abs_factory import AbsFactory


def load_factory(factory_name):
    try:
        factory_module = import_module("." + factory_name, "factories")
    except ImportError:
        factory_module = import_module(".nullcar_factory", "factories")

    classes = getmembers(factory_module, lambda m: isclass(m) and not isabstract(m))

    for _, _class in classes:
        if issubclass(_class, AbsFactory):
            return _class()
