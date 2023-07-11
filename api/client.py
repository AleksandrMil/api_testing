import requests


# Этот метод класса Client объявлен с использованием декоратора @staticmethod,
# что означает, что метод может быть вызван без создания экземпляра класса.
# Метод get выполняет HTTP-запрос типа GET на указанный url с использованием функции requests.request
# и возвращает результат этого запроса.
class Client:

    @staticmethod
    def get(url, timeout=5):
        return requests.request('GET', url, timeout=timeout)

    @staticmethod
    def post(url, headers, payload, timeout=5):
        return requests.request("POST", url, headers=headers, data=payload, timeout=timeout)

    @staticmethod
    def delete(url, timeout=5):
        return requests.request("DELETE", url, timeout=timeout)
