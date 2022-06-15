import asyncio
import itertools
import sys


async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            # use asyncio.sleep() instead of time.sleep() to sleep without
            # blocking the event loop
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))


# slow_function() now is coroutine in which `await` is used so that the event
# loop can continue to run while coroutine is sleeping simulating I/O
async def slow_function():
    await asyncio.sleep(3)
    return 42


async def supervisor():
    # asyncio.ensure_future() shedules the execution of coroutine `spin`
    # by wrapping it with a `Task` object, which returns immediately
    spinner = asyncio.ensure_future(spin('thinking!'))
    print('spinner object:', spinner)
    result = await slow_function()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
