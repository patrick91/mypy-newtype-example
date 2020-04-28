def make_union(name, types):
    return 1


Result = make_union("Example", (int, str))


def process() -> Result:
    ...


reveal_type(process)