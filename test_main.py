import sys

import pytest
from main import main


URLS = [
    'https://www.google.com/',
    'https://dzen.ru',
    'some_string',
    'not_urls',
    'https://www.avito.ru/',
    'https://ya.ru/',
    'www.facebook.com',
    'vk.ru',
    'vk.net',
]


def test_main(capsys):
    main()
    for i in URLS:
        sys.stderr.write(i)
        sys.stderr.write('')
    out, err = capsys.readouterr()
    print(out)
