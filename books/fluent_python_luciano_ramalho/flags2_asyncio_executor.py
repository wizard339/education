import asyncio
import collections

import aiohttp
from aiohttp import web
import tqdm

from flags2_common import main, HTTPStatus, Result, save_flag

# by default, we set a small value
DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000


# this exception is needed for wrapping exceptions of web and HTTP, in order to
# add a field `country_code` to them
class FetchError(Exception):
    def __init__(self, country_code):
        self.country_code = country_code


async def get_flag(base_url, cc):
    url = '{}/{cc}.png'.format(base_url, cc=cc.lower())
    resp = await aiohttp.request('GET', url)
    if resp.status == 200:
        image = await resp.read()
        return image
    elif resp.status == 404:
        raise web.HTTPNotFound()
    else:
        raise aiohttp.HTTPProcessingError(code=resp.status,
                                          message=resp.reason,
                                          headers=resp.headers)


# `semaphore` is object of class `asyncio.Semaphore`, synchronization mechanism
# that limits the number of concurent requests, so as not to block the whole
# system: only this coroutine is blocked when the semaphore counter will reaches
# the maximum allowed value
async def download_one(cc, base_url, semaphore, verbose):
    try:
        # semaphore uses as context manager in await expression
        with await semaphore:
            image = await get_flag(base_url, cc)
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, save_flag, image, cc.lower( + '.png'))
        status = HTTPStatus.ok
        msg = 'OK'

    if verbose and msg:
        print(cc, msg)

    return Result(status, cc)


async def downloader_coro(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    # create a semaphore object, which allows to run no more than `concur_req`      # coroutines at the same time
    semaphore = asyncio.Semaphore(concur_req)
    to_do = [download_one(cc, base_url, semaphore, verbose)
            for cc in sorted(cc_list)]
    
    # this iterator will return future objects as they are completed
    to_do_iter = asyncio.as_completed(to_do)
    if not verbose:
        to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))

    for future in to_do_iter:
        try:
            res = await future
        except FetchError as exc:
            # get the country code from the object, when downloading the flag
            # of which an exception occurred
            country_code = exc.country_code
            # try to get a message about exception from the original exception
            # object
            try:
                error_msg = exc.__cause__.args[0]
            # if in original exception not message about exception, use a name
            # of class of original exception
            except IndexError:
                error_msg = exc.__cause__.__class__.__name__
            if verbose and error_msg:
                msg = '*** Error for {}: {}'
                print(msg.format(country_code, error_msg))
            status = HTTPStatus.error
        else:
            status = res.status

        counter[status] += 1

    return counter


def download_many(cc_list, base_url, verbose, concur_req):
    loop = asyncio.get_event_loop()
    coro = downloader_coro(cc_list, base_url, verbose, concur_req)
    counts = loop.run_until_complete(coro)
    loop.close()

    return counts


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
