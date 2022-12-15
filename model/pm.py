from pathlib import Path
from sys import path

from .states import StatesManager
from utils.constants import pathlike

__all__ = [
    'PersistenceManager',
]


# КОММЕНТАРИЙ: ждал-ждал обновлений, так и не дождался

class PersistenceManager:
    default_states_path = Path(path[0]) / 'states.json'
    default_parameters_path = Path(path[0]) / 'parameters.json'

    @classmethod
    # ИСПРАВИТЬ: что такое default_read? если исходить из того, как вы его используете, то здесь должен быть параметр для как раз нестандартного пути
    def read_parameters(cls, default_read=None):
        if not default_read:
            default_read = cls.default_states_path
        # ИСПРАВИТЬ: и зачем было создавать атрибут класса для пути, параметр метода для пути, если в итоге вы передаёте в open() строковый литерал?
        with open('parameters.json') as f:
            # КОММЕНТАРИЙ: сразу видно, тесты вы не делаете — импорта не хватает, но кого ж это волнует, запускать код ведь всё равное не надо...
            parameters = json.load(f)
        # ДОБАВИТЬ: файл может отсутствовать; может присутствовать, но быть пустым; может не быть пустым, но в нём совсем другие данные — не думаю, что стоит так вот лихо брать и сразу возвращать даже не зная что именно: словарь там, или список, или ещё что-то
        return parameters

    @classmethod
    def write_file(cls, default_save):
        with open('states.json', 'w', encoding='utf-8') as f:
            json.dump(default_save, f, indent=4)

    @classmethod
    def read_state(cls, default_read=None):
        if not default_read:
            default_read = cls.default_states_path
        # ДОБАВИТЬ: записывать надо тоже в кодировке utf-8
        with open('states.json') as f:
            states = json.load(f)
        return StatesManager(states['kind'],
                             states['name'],
                             states['birthday'],
                             states["mind_state"],
                             states["body_state"],
                             # ИСПРАВИТЬ: метод to_dict() возвращает словарь, а не экземпляр StatesManager — зачем с помощью словаря states создавать экземпляр StatesManager, а потом от него возвращать словарь? если хотите вернуть словарь, то возвращайте сразу states (убедившись, что там всё в порядке, и что это словарь)
                             ).to_dict()
