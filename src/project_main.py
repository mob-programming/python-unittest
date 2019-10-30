#!/usr/bin/env python3

### FIZZ BUZZ

# Fizz Buzz

# F


class ProjectMain:

    def __init__(self, param) -> None:
        for i in range(1, param+1):
            print(self.fizzbuzz(i))

    def fizzbuzz(self, param):
        if param % 3 == 0 and param % 5 == 0:
            return "FizzBuzz"
        elif param % 3 == 0:
            return "Fizz"
        elif param % 5 == 0:
            return "Buzz"
        else:
            return param

def main():
    ProjectMain(100)

if __name__ == "__main__":
    main()

