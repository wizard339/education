import doctest


class ArithmeticProgression:
    
    """
    class ``ArithmeticProgression``
    
        >>> ap = ArithmeticProgression(0, 1, 3)
        >>> list(ap)
        [0, 1, 2]
        >>> ap = ArithmeticProgression(1, .5, 3)
        >>> list(ap)
        [1.0, 1.5, 2.0, 2.5]
        >>> ap = ArithmeticProgression(0, 1/3, 1)
        >>> list(ap)
        [0.0, 0.3333333333333333, 0.6666666666666666]
        >>> from fractions import Fraction
        >>> ap = ArithmeticProgression(0, Fraction(1, 3), 1)
        >>> list(ap)
        [Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]
        >>> from decimal import Decimal
        >>> ap = ArithmeticProgression(0, Decimal('.1'), .3)
        >>> list(ap)
        [Decimal('0'), Decimal('0.1'), Decimal('0.2')]
    """
    
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end # None -> infinite row
        
    def __iter__(self):
        result = type(self.begin + self. step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index
    
        
if __name__=='__main__':
    doctest.testmod(verbose=True)
