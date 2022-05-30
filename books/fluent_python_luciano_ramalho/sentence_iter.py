import re
import reprlib
import doctest

RE_WORD = re.compile('\w+')

class Sentence:
    
    """
    class ``Sentence``
    
        >>> s = Sentence('"The time has come," the Walrus said,')
        >>> s
        Sentence('"The time ha... Walrus said,')
        >>> for word in s:
        ...     print(word)
        The
        time
        has
        come
        the
        Walrus
        said
        >>> list(s)
        ['The', 'time', 'has', 'come', 'the', 'Walrus', 'said']
    """
    
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        return SentenceIterator(self.words)
        

class SentenceIterator:
    
    def __init__(self, words):
        self.words = words
        self.index = 0
        
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word
    
    def __iter__(self):
        return self
        
if __name__=='__main__':
    doctest.testmod(verbose=True)
