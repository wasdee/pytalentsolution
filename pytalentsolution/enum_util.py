from enum import Enum


class AutoName(Enum):
    """
    https://docs.python.org/3/library/enum.html#using-automatic-values
    """
    def _generate_next_value_(name, start, count, last_values):
        return name