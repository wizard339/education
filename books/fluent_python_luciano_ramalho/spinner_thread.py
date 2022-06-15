import threading
import itertools
import time
import sys


class Signal:
    go = True


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        # return the cursor back by typing the symbols of backspace
        write('\x08' * len(status))
        time.sleep(0.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    # simulate waiting for the completion of a lengthy
    # I/O operation
    time.sleep(5)
    return 42


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin,
                               args=('thinking!', signal))
    # displaying the object of the second thread
    print('spinner object:', spinner)
    # run the second thread
    spinner.start()
    # call `slow_function`, and the main thread is blocked.
    # meanwhile, the indicator is animated by the second stream
    result = slow_function()
    # change the state of `signal`, thus we complete cycle inside `spin`
    signal.go = False
    # waiting the end of thread `spinner`
    spinner.join()
    return result


def main():
    result = supervisor()
    print('Answer:', result)


if __name__ == '__main__':
    main()
