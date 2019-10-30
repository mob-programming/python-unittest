#!/usr/bin/env python3

### FIZZ BUZZ

# Fizz Buzz

# F


class ProjectMain:

    def __init__(self) -> None:
        pass

    def fizzbuzz(self, param):
        if param % 3 == 0 and param % 5 == 0:
            return "FizzBuzz"
        elif param % 3 == 0:
            return "Fizz"
        elif param % 5 == 0:
            return "Buzz"
        else:
            return param