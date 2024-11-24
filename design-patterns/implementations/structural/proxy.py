from abc import ABC, abstractmethod


class API(ABC):
    @abstractmethod
    def request(self):
        pass


class ProtectedAPI(API):
    def __init__(self):
        self.is_authorized = False

    def authorize(self):
        self.is_authorized = True

    def request(self):
        if self.is_authorized:
            print("POST request successful")
        else:
            raise Exception("User not authorized")


class ProtectedAPIProxy(API):
    def __init__(self, protected_api):
        self.protected_api = protected_api

    def request(self):
        self.protected_api.authorize()
        self.protected_api.request()


if __name__ == '__main__':
    api = ProtectedAPI()
    proxy = ProtectedAPIProxy(api)
    proxy.request()
