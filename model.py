import datetime
from enum import Enum
from datetime import date


class Kind(Enum):
    CAT = 'Cat'
    DOG = 'Dog'
    FOX = 'Fox'
    BEAR = 'Bear'
    SNAKE = 'Snake'


class Mind:
    # pattern: Dict(дописать!)
    def __init__(self, joy: int, anger: int):
        self.joy = joy
        self.anger = anger


class Body:
    def __init__(self, health: int, stamina: int, hunger: int, thirst: int):
        self.health = health
        self.stamina = stamina
        self.hunger = hunger
        self.thirst = thirst


class Creature:
    def __init__(self, kind: Kind, name: str, birthday, body: Body, mind: Mind):
        self.kind = kind
        self.name = name
        self.birthday = birthday
        self.body = body
        self.mind = mind

    def age(self):
        return date.today() - self.birthday  # Доделать нормальный формат времени


class BodyState:
    def __init__(self, timestamp: datetime, health: int, stamina: int, hunger: int, thirst: int):
        self.timestamp = timestamp
        self.health = health
        self.stamina = stamina
        self.hunger = hunger
        self.thirst = thirst


class MindState:
    # add pattern!!!
    def __init__(self, timestamp: datetime, joy: int, anger: int):
        self.timestamp = timestamp
        self.joy = joy
        self.anger = anger


class StatesManager:
    pass


class PersistenceManager:
    pass


class StatesCalculator:
    pass


class CreatureActions:
    pass
