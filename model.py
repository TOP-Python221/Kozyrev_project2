import datetime
import json
from pathlib import Path
from enum import Enum
from datetime import datetime as dt
from sys import path


class Kind(Enum):
    CAT = 'Cat'
    DOG = 'Dog'


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
    def __init__(self, kind: Kind, name: str, birthday, body: Body, mind: Mind):
        self.kind = kind
        self.name = name
        self.birthday = birthday
        self.body = body
        self.mind = mind

    def age(self):
        return dt.now() - self.birthday.day  # Доделать нормальный формат времени

    def __str__(self):
        pass


class BodyState:
    def __init__(self, timestamp: datetime, health=0, stamina=0, hunger=0, thirst=0):
        self.timestamp = timestamp
        self.health = health
        self.stamina = stamina
        self.hunger = hunger
        self.thirst = thirst

    def to_dict(self):
        value_for_dict = [self.timestamp, self.health, self.stamina, self.hunger, self.thirst]
        key_for_dict = ['timestamp', 'health', 'stamina', 'hunger', 'thirst']
        body_state = dict()
        for key, value in zip(key_for_dict, value_for_dict):
            body_state[key] = value
        return body_state


class MindState:
    # add pattern!!!
    def __init__(self, timestamp: datetime, joy=10, anger=10):
        self.timestamp = timestamp
        self.joy = joy
        self.anger = anger

    def to_dict(self) -> dict:
        value_for_dict = [self.timestamp, self.joy, self.anger]
        key_for_dict = ['timestamp', 'joy', 'anger']
        mind_state = dict()
        for key, value in zip(key_for_dict, value_for_dict):
            mind_state[key] = value
        return mind_state


class StatesManager:
    def __init__(self, pet: Kind, name: str, birthday: dt, body_last: BodyState, mind_last: MindState):
        self.pet = pet
        self.name = name
        self.birthday = birthday
        self.body_last = body_last
        self.mind_last = mind_last

    def to_dict(self):
        value_for_dict = [self.pet, self.name, self.birthday]
        key_for_dict = ['kind', 'name', 'birthday']
        states = dict()
        for key, value in zip(key_for_dict, value_for_dict):
            states[key] = value
        states['mind_state'] = self.mind_last
        states['body_state'] = self.body_last
        return states


class PersistenceManager:
    default_states_path = Path(path[0]) / 'states.json'

    @classmethod
    def read_parameters(cls):
        pass

    @classmethod
    def write_file(cls, default_save):
        with open('states.json', 'w', encoding='utf-8') as f:
            json.dump(default_save, f, indent=4)

    @classmethod
    def read_state(cls, default_read=None):
        if not default_read:
            default_read = cls.default_states_path
        with open('states.json') as f:
            parameters = json.load(f)

        return StatesManager(parameters['kind'],
                             parameters['name'],
                             parameters['birthday'],
                             parameters["mind_state"],
                             parameters["body_state"],
                             ).to_dict()


# Тесты!!! Создания нового питомца. С начала создается экземпляры классов BodyState and MindState с параметрами
# по умолчанию(пример) и передачи их аргументом в экземпляр класса StateManager. и после создания, сохранение
# в фаил. Дальше можно передавать его параметром в класс StatesCalculator и от него использовать методы revive...
#

# vremy = dt.now().strftime('%Y-%m-%d %H:%M:%S')
# body = BodyState(vremy).to_dict()
# mind = MindState(vremy).to_dict()
# kind = Kind.CAT.value
# pets = StatesManager(kind, 'Mars', vremy, body, mind).to_dict()
#
# PersistenceManager.write_file(pets)

# print(PersistenceManager.read_file())


class StatesCalculator:
    def __init__(self, previous: StatesManager):
        self.previous = previous

    def new_body(self) -> Body:
        pass

    def new_mind(self) -> Mind:
        pass


class CreatureActions:
    pass
