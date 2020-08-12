#!/usr/bin/env python3


class ProjectMain:

    data = dict()

    def __init__(self) -> None:
        pass

    def get_greeting(self) -> str:
        return self.data.get('greeting')

    def set_greeting(self, greeting: str = 'Hello user!') -> None:
        self.data.setdefault('greeting', greeting)

class Board:

    def __init__(self, width, height) -> None:
        pass

    def set_alive(self, param, param1):
        pass

    def get_state(self, param, param1):
        return False

    def move(self):
        pass
