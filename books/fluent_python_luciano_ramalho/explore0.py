import doctest
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

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    
