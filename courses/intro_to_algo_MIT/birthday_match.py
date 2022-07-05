class StaticArray:
    def __init__(self, n):
        self.data = [None] * n

    def get_at(self, index):
        if not (0 <= index < len(self.data)):
            raise IndexError
        return self.data[index]

    def set_at(self, index, value):
        if not (0 <= index < len(self.data)):
            raise IndexError
        self.data[index] = value


def birthday_match(students):
    """
    Find a pair of students with the same birthday
    Input:  tuple of student (name, bday) tuples
    Output: tuple of student names or None
    """
    n = len(students)                            # O(1)
    record = StaticArray(n)                      # O(n)
    for k in range(n):                           # n
        (name1, bday1) = students[k]             # O(1)
        # return pair if bdayl in record
        for i in range(k):                       # k
            (name2, bday2) = record.get_at(i)    # O(1)
            if bday1 == bday2:                   # O(1)
                return (name1, name2)            # O(1)
        record.set_at(k, (name1, bday1))         # O(1)
    return None                                  # O(1)

# RUNNING TIME ANALYSIS
# Two loops: outer k = {0, ..., n-1}, inner is i = {0, ..., k}
# Running time is O(n) + sum(O(1) + k*O(1)) = O(n*n)
# Quadratic in n is polynomial
