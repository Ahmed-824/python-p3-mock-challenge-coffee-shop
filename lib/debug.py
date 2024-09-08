#!/usr/bin/env python3
import ipdb # type: ignore

if ipdb is None:
    import pdb as ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    ipdb.set_trace()
