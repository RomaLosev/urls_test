from concurrent.futures import ThreadPoolExecutor

import requests
from validator_collection import checkers


methods = {
    'GET': requests.get,
    'POST': requests.post,
    'PUT': requests.put,
    'DELETE': requests.delete,
    'HEAD': requests.head,
    'PATCH': requests.patch,
    'OPTIONS': requests.options,
}


def get_response(url: str) -> dict:
    result = {}
    for method, req in methods.items():
        code = req(url).status_code
        if not code == 405:
            result[method] = code
    return {url: result}


def execute(urls: list) -> dict:
    result = {}
    with ThreadPoolExecutor() as executor:
        future = executor.map(get_response, urls)
        for url in future:
            for key, value in url.items():
                result[key] = value
    return result


def url_checker(urls: list) -> list:
    true_urls = []
    for item in urls:
        if checkers.is_url(item):
            true_urls.append(item)
        else:
            print(f'String {item} is not a link')
    return true_urls


def main(urls: list = None):
    if not urls:
        urls = list(iter(input, ''))
    true_urls = url_checker(urls)
    result = execute(true_urls)
    print(result)


if __name__ == '__main__':
    main()
