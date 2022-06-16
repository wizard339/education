from urllib.request import urlopen
import warnings
import os
import json


URL = 'https://searchcode.com/codesearch/raw/99786584/'
JSON = 'data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)
