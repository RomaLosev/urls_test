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


class TestAPP:

    def test_main_with_list(self, capsys):
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
                    "'https://ya.ru/': "
                    "{'GET': 200, 'POST': 200, 'PUT': 200, 'DELETE': 200, 'HEAD': 302, 'PATCH': 200, 'OPTIONS': 200}}\n")
        assert out == expected

    def test_main_with_input(self, capsys):
        input_values = ['https://dzen.ru', 'string', '']

        def mock_input():
            return input_values.pop(0)

        main.input = mock_input
        main.main()
        out, err = capsys.readouterr()
        expected = ("String string is not a link\n"
                    "{'https://dzen.ru': {'GET': 200}}\n")
        assert out == expected


class TestModules:
    URLS = ['string', '', 'https://dzen.ru', 'www.nothing.com', 'https://www.avito.ru/']

    def test_get_response(self):
        result = main.get_response('https://dzen.ru')
        expected = {'https://dzen.ru': {'GET': 200}}
        assert result == expected

    def test_url_checker(self):
        urls = ['string', '', 'https://dzen.ru', 'www.nothing.com', 'https://www.avito.ru/']
        result = main.url_checker(urls)
        expected = ['https://dzen.ru', 'https://www.avito.ru/']
        assert result == expected

    def test_execute(self):
        urls = ['https://dzen.ru', 'https://www.avito.ru/']
        result = main.execute(urls)
        expected = {
            'https://dzen.ru': {'GET': 200},
            'https://www.avito.ru/': {
                'GET': 403, 'POST': 403, 'PUT': 403, 'DELETE': 403, 'HEAD': 403, 'PATCH': 403, 'OPTIONS': 403
            }
        }
        assert result == expected
