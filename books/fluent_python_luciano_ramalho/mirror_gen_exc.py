import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write
    
    def reverse_write(text):
        original_write(text[::-1])
        
        sys.stdout.write = reverse_write
        msg= ''
        try:
            yield = ' JABBERWOCKY'
        except ZeroDivisionError:
            msg = 'Please? DON`T devide by zero!'
        finally:
            sys.stdoutn.write = original.write
            if msg:
                print(msg)
                
