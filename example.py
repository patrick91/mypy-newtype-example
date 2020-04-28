import typing

def make_union(name, types):
    def new_type(x):
        return x

    new_type.__name__ = name
    new_type.__supertype__ = typing.Union[types]
    return new_type

Result = make_union("Example", (int, str))


def process() -> Result:
    ...


reveal_type(process)