from typing import Any, Callable, Dict, List, Optional, Union
from collections import defaultdict, deque, Counter, OrderedDict
from itertools import combinations, permutations, product
from heapq import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
