from concurrent.futures import ThreadPoolExecutor

import requests
from validator_collection import checkers


def get_response(url: str) -> dict:
    get = requests.get(url)
    post = requests.post(url)
    put = requests.put(url)
    delete = requests.delete(url)
    head = requests.head(url)
    patch = requests.patch(url)
    options = requests.options(url)
    request_methods = [get, post, put, delete, head, patch, options]
    result = {}
    for method in request_methods:
        if not method.status_code == 405:
            result[method.request.method] = method.status_code
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
