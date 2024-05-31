import json
from random import choice

import importlib_resources

from random_horror.loaders import PackageListLoader
from random_horror.loaders.base import ListLoader


class RandomHorrorGenerator(object):
    def __init__(self, list_loader: ListLoader = None):
        if list_loader is None:
            list_loader = PackageListLoader()

        # For each valid list name, load the list using the appropriate Loader
        # class and create an attribute using that list name
        for list_name in ListLoader.VALID_LIST_NAMES:
            setattr(self, list_name, list_loader.load_word_list(list_name))

    def pick_items(self, item_count):
        items = []
        for x in range(item_count):
            items.append(choice(getattr(self, ListLoader.LIST_ITEMS)))
        return items

    def randomise(self, choice_count: int, items_count: int = 5) -> list[dict]:
        generated_objects = []

        for x in range(choice_count):
            pick = {}

            pick['who'] = " ".join([
                choice(getattr(self, ListLoader.LIST_WHO_ADJECTIVES)),
                choice(getattr(self, ListLoader.LIST_WHO_NOUNS)),
            ])

            pick['place'] = " ".join([
                choice(getattr(self, ListLoader.LIST_PLACE_ADJECTIVES)),
                choice(getattr(self, ListLoader.LIST_PLACE_NOUNS)),
            ])

            pick['plot_device'] = choice(getattr(self, ListLoader.LIST_PLOT_DEVICES))

            pick['random_items'] = self.pick_items(items_count)

            generated_objects.append(pick)

        return generated_objects
