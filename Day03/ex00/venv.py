#!/usr/bin/env python3
import os

if __name__ == '__main__':
    print(f"Your current virtual env is {os.environ['VIRTUAL_ENV']}")


# python3 -m venv mmago
# source mmago/bin/activate
# deactivate