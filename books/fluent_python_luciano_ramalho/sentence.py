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
        
    def __getitem__(self, index):
        return self.words[index]
        
    def __len__(self):
        return len(self.words)
        
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
        
        
if __name__=='__main__':
    doctest.testmod(verbose=True)
