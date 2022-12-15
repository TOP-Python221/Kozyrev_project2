from utils.constants import KindActions
from datetime import datetime as dt

__all__ = [
    'Creature',
    'Body',
    'Mind',
]


class Mind:  # momento
    def __init__(self, joy: int, anger: int):
        self.joy = joy
        self.anger = anger


class Body:  # momento
    def __init__(self, health: int, stamina: int, hunger: int, thirst: int):
        self.health = health
        self.stamina = stamina
        self.hunger = hunger
        self.thirst = thirst


class Creature:
    def __init__(self, kind: KindActions, name: str, birthday, body: Body, mind: Mind):
        self.kind = kind
        self.name = name
        self.birthday = birthday
        self.body = body
        self.mind = mind

    def age(self):
        return (dt.now() - self.birthday).days
        # КОММЕНТАРИЙ: это ерунда, вы с моделью и её реализацией сначала разберитесь
        # Доделать нормальный формат времени

    def __str__(self):
        pass


class CreatureActions:
    pass
