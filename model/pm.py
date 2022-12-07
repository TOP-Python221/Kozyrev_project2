from pathlib import Path
from sys import path

from .states import StatesManager
from utils.constants import pathlike

__all__ = [
    'PersistenceManager',
]


class PersistenceManager:
    default_states_path = Path(path[0]) / 'states.json'
    default_states_path = Path(path[0]) / 'parameters.json'

    @classmethod
    def read_parameters(cls, default_read=None):
        if not default_read:
            default_read = cls.default_states_path
        with open('parameters.json') as f:
            parameters = json.load(f)
        return parameters

    @classmethod
    def write_file(cls, default_save):
        with open('states.json', 'w', encoding='utf-8') as f:
            json.dump(default_save, f, indent=4)

    @classmethod
    def read_state(cls, default_read=None):
        if not default_read:
            default_read = cls.default_states_path
        with open('states.json') as f:
            states = json.load(f)
        return StatesManager(states['kind'],
                             states['name'],
                             states['birthday'],
                             states["mind_state"],
                             states["body_state"],
                             ).to_dict()
