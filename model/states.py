from .creature import Body, Mind, Creature

__all__ = [
    'StatesManager',
    'StatesCalculator',
]


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


class StatesCalculator:
    def __init__(self, previous: StatesManager):
        self.previous = previous

    def new_body(self) -> Body:
        pass

    def new_mind(self) -> Mind:
        pass
