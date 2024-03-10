class ExampleClass[**P]:
    """
    example class
    """
    def __init__(self, *args: P.args, **kwargs: P.kwargs):
        ...


def example_function[**P](cls: type[ExampleClass[P]]) -> type[ExampleClass[P]]:
    """
    example function
    """
    return cls
