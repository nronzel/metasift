from enum import Enum


# ANSI colors for console output
class Color(Enum):
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    CYAN = "\033[0;36m"
    RESET = "\033[0m"
