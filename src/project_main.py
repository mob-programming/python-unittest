#!/usr/bin/env python3


class ProjectMain:

    def __init__(self) -> None:
        pass

    @staticmethod
    def process_integer(current_integer):
        if current_integer % 15 == 0:
            return "FizzBuzz"
        elif current_integer % 3 == 0:
            return "Fizz"
        elif current_integer % 5 == 0:
            return "Buzz"
        else:
            return current_integer
