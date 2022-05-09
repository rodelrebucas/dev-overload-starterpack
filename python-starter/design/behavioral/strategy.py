#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://stackoverflow.com/questions/963965/how-is-this-strategy-pattern
 -written-in-python-the-sample-in-wikipedia
In most of other languages Strategy pattern is implemented via creating some
base strategy interface/abstract class and subclassing it with a number of
concrete strategies (as we can see at
http://en.wikipedia.org/wiki/Strategy_pattern), however Python supports
higher-order functions and allows us to have only one class and inject
functions into it's instances, as shown in this example.

*TL;DR80
Enables selecting an algorithm at runtime.
"""

import types


class StrategyExample:
    def __init__(self, func=None):
        self.name = "Strategy Example 0"
        if func is not None:
            # types.MethodType(func, self) in each execute replacements:
            # <bound method execute_replacement1 of <__main__.StrategyExample object at 0x7f16b0fcd908>>
            # <bound method execute_replacement2 of <__main__.StrategyExample object at 0x7f16b0fcd908>>
            self.execute = types.MethodType(func, self)

    # <bound method StrategyExample.execute of <__main__.StrategyExample object at 0x7f16b0fcd908>>
    def execute(self):
        print(self.name)


def execute_replacement1(self):
    print(self.name + " from execute 1")


def execute_replacement2(self):
    print(self.name + " from execute 2")


if __name__ == "__main__":
    strat0 = StrategyExample()

    strat1 = StrategyExample(execute_replacement1)
    strat1.name = "Strategy Example 1"

    strat2 = StrategyExample(execute_replacement2)
    strat2.name = "Strategy Example 2"

    strat0.execute()
    strat1.execute()
    strat2.execute()

### OUTPUT ###
# Strategy Example 0
# Strategy Example 1 from execute 1
# Strategy Example 2 from execute 2
