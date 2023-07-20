from src.item import Item


class MixinLanguage:

    def change_lang(self):
        self._language = "RU" if self._language == "EN" else "EN"
        return self


class Keyboard(Item, MixinLanguage):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._language = "EN"

    @property
    def language(self):
        return self._language
