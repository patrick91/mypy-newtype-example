from typing import Callable, Optional

from mypy.nodes import TypeAlias, PlaceholderNode, Node
from mypy.types import Type, TypeAliasType, UnionType, AnyType, PlaceholderType, TypeStrVisitor
from mypy.plugin import ClassDefContext, Plugin, FunctionContext, AnalyzeTypeContext
from mypy.plugins import dataclasses



def union_hook(ctx) -> Type:
    return PlaceholderType(None, args=[AnyType(2)], line=-1)


class UPlugin(Plugin):
    def get_function_hook(self, fullname: str) -> Optional[Callable[[FunctionContext], Type]]:
        if fullname == "example.make_union":
            return union_hook

        return None


def plugin(version: str):
    return UPlugin
