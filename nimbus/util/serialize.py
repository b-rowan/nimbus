def to_cgminer(snake: str) -> str:
    """
    Generate CGMiner style output aliases.

    These aliases have each word capitalized and are separated by spaces.

    Args:
        snake: The python or snake case name of the attribute.
    """

    return snake.title().replace("_", " ")


def to_upper(snake: str) -> str:
    """
    Generate uppercased output aliases.

    Args:
        snake: The python or snake case name of the attribute.
    """

    return snake.upper()
