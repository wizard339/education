import asyncio
import collections

import aiohttp
from aiohttp import web
import tqdm

from flags2_common import main, HTTPStatus, Result, save_flag

# by default, we set a small value
DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000


# this exception is needed for wrapping exceptions of web and HTTP,
# in order to add a field `country_code` to them
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


# `semaphore` is object of class `asyncio.Semaphore`, synchronization
# mechanism that limits the number of concurent requests, so as not to
# block the whole system: only this coroutine is blocked when the
# semaphore counter will reaches the maximum allowed value
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
        save_flag(image, cc.lower() + '.png')
        status = HTTPStatus.ok
        msg = 'OK'

    if verbose and msg:
        print(cc, msg)

    return Result(status, cc)


async def downloader_coro(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req)
