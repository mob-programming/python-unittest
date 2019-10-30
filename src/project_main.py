#!/usr/bin/env python3

### FIZZ BUZZ

#Fizz Buzz

#F



class ProjectMain:

    data = dict()

    def __init__(self) -> None:
        pass

    def get_greeting(self) -> str:
        return self.data.get('greeting')

    def set_greeting(self, greeting: str = 'Hello user!') -> None:
        self.data.setdefault('greeting', greeting)

    def is_number(self, param):
        return False

    def fizzbuzz(self, param):
        if param % 3 == 0:
            return "Fizz"
        elif param % 5 == 0:
            return "Buzz"
    
    