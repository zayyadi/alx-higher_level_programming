#!/usr/bin/python3
from typing import List

def element_at(my_list: List, idx: int) -> int:
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]
