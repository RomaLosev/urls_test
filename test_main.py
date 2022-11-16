import main

URLS = [
    'https://www.google.com/',
    'https://dzen.ru',
    'some_string',
    'not_url',
    'https://www.avito.ru/',
    'https://ya.ru/',
    'www.facebook.com',
    'vk.ru',
    'vk.net',
]


def test_main_with_list(capsys):
    main.main(URLS)
    out, err = capsys.readouterr()
    expected = ("String some_string is not a link\n"
                "String not_url is not a link\n"
                "String www.facebook.com is not a link\n"
                "String vk.ru is not a link\n"
                "String vk.net is not a link\n"
                "{'https://www.google.com/': {'GET': 200, 'HEAD': 200}, "
                "'https://dzen.ru': {'GET': 200}, "
                "'https://www.avito.ru/': "
                "{'GET': 403, 'POST': 403, 'PUT': 403, 'DELETE': 403, 'HEAD': 403, 'PATCH': 403, 'OPTIONS': 403}, "
                "'https://ya.ru/': {'GET': 200, 'HEAD': 302}}\n")
    assert out == expected


def test_get_response():
    result = main.get_response('https://dzen.ru')
    expected = {'https://dzen.ru': {'GET': 200}}
    assert result == expected


def test_main_with_input(capsys):
    input_values = ['https://dzen.ru', 'string', '']

    def mock_input():
        return input_values.pop(0)
    main.input = mock_input
    main.main()
    out, err = capsys.readouterr()
    expected = ("String string is not a link\n"
                "{'https://dzen.ru': {'GET': 200}}\n")
    assert out == expected
