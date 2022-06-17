import doctest
import keyword
from collections import abc


class FrozenJSON:
    """
    a read-only facade for navigating a JSON-like object using attribute notation

    Tests for doctest:
        >>> from osconfeed import load
        >>> raw_feed = load()
        >>> feed = FrozenJSON(raw_feed)
        >>> len(feed.Schedule.speakers)
        356
        >>> sorted(feed.Schedule.keys())
        ['conferences', 'events', 'speakers', 'venues']
        >>> for key, value in sorted(feed.Schedule.items()):
        ...     print('{:3}  {}'.format(len(value), key))
          1  conferences
        485  events
        356  speakers
         53  venues
        >>> feed.Schedule.speakers[-1].name
        'Carina C. Zona'
        >>> talk = feed.Schedule.events[40]
        >>> type(talk)
        <class '__main__.FrozenJSON'>
        >>> talk.name
        'There *Will* Be Bugs'
        >>> talk.speakers
        [3471, 5199]
        >>> talk.flavor
        Traceback (most recent call last):
         ...
        KeyError: 'flavor'
    """
    # `__new__` uses instead of `build` for constructing new objects
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])


if __name__ == '__main__':
    doctest.testmod(verbose=True)
