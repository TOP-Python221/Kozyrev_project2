from enum import Enum
from pathlib import Path
from collections.abc import Sequence, Callable
from typing import Annotated, TypedDict


class Kind(Enum):
    CAT = 'Cat'
    DOG = 'Dog'


pathlike = str | Path


class KindActions:
    pass