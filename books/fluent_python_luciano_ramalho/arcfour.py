"""compatible with algorithm RC4"""

def arcfour(key, in_bytes, loops=20):
    
    # create key box
    kbox = bytearray(256)
    # copy key and vector
    for i, car in enumerate(key):
        kbox[i] = car
    j = len(key)
    # repeat until full
    for i in range(j, 256):
        kbox[i] = kbox[i-j]
        
    # initialize sbox
    sbox = bytearray(range(256))
    
    # repeat the cycle mixing sbox as recommended in CipherSaber-2
    j = 0
    for k in range(loops):
        for i in range(256):
            j = (j + sbox[i] + kbox[i]) % 256
            sbox[i], sbox[j] = sbox[j], sbox[i]
            
        # main cycle
        i = 0
        j = 0
        out_bytes = bytearray()
        
        for car in in_bytes:
            i = (i + 1) % 256
            # mixing sbox
            j = (j + sbox[i]) % 256
            sbox[i], sbox[j] = sbox[j], sbox[i]
            # compute t
            t = (sbox[i] + sbox[j]) % 256
            k = sbox[t]
            car = car ^ k
            out_bytes.append(car)
            
        return out_bytes
        
def test():
    from time import time
    clear = bytearray(b'1234567890' * 100000)
    t0 = time()
    cipher = arcfour(b'key', clear)
    print('elapsed time: %.2fs' % (time() - t0))
    result = arcfour(b'key', cipher)
    assert result == clear, '% != %r' % (result, clear)
    print('elapsed time: %.2fs' % (time() - t0))
    print('OK')
    
if __name__=='__main__':
    test()
    
