
class ListLoader(object):
    LIST_WHO_NOUNS = "who_nouns"
    LIST_WHO_ADJECTIVES = "who_adjectives"
    LIST_PLOT_DEVICES = "plot_devices"
    LIST_ITEMS = "items"
    LIST_PLACE_ADJECTIVES = "place_adjectives"
    LIST_PLACE_NOUNS = "place_nouns"

    VALID_LIST_NAMES = [
        LIST_WHO_NOUNS,
        LIST_WHO_ADJECTIVES,
        LIST_PLOT_DEVICES,
        LIST_ITEMS,
        LIST_PLACE_ADJECTIVES,
        LIST_PLACE_NOUNS,
    ]

    def __init__(self):
        pass

    def load_word_list(self, list_name: str, src: str = None) -> list[str]:
        pass
