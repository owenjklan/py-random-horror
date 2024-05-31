from importlib_resources import files

from random_horror.loaders.base import ListLoader


class PackageListLoader(ListLoader):
    """
    Loads lists from files contained within the
    package itself.
    """
    DEFAULT_LIST_RESOURCES = {
        ListLoader.LIST_WHO_ADJECTIVES: "who_adjectives.txt",
        ListLoader.LIST_WHO_NOUNS: "who_nouns.txt",
        ListLoader.LIST_PLOT_DEVICES: "plot_devices.txt",
        ListLoader.LIST_ITEMS: "misc.txt",
        ListLoader.LIST_PLACE_ADJECTIVES: "place_adjectives.txt",
        ListLoader.LIST_PLACE_NOUNS: "place_nouns.txt",
    }

    def load_word_list(self, list_name: str, src: str = None) -> list[str]:
        if list_name not in self.VALID_LIST_NAMES:
            raise ValueError(f"Invalid list name: {list_name}")

        if src is None:
            resource_path = self.DEFAULT_LIST_RESOURCES[list_name]
        else:
            resource_path = src

        list_lines = files('random_horror.lists').joinpath(resource_path).read_text().splitlines()

        return [
            line.strip() for line in list_lines if len(line.strip()) > 0
        ]
