from enum import Enum
from pathlib import Path
from collections.abc import Sequence, Callable
from typing import Annotated, TypedDict


class Kind(Enum):
    CAT = 'Cat'
    DOG = 'Dog'


pathlike = str | Path


# ИСПРАВИТЬ: это не класс, а переменная ссылающаяся на объекты абстрактных классов — для аннотации
class KindActions:
    pass
