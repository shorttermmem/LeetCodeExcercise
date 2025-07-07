#https://leetcode.com/problems/process-restricted-friend-requests/description/
from common_types import *

"""
You are given an integer n indicating the number of people in a network. Each person is labeled from 0 to n - 1.

You are also given a 0-indexed 2D integer array restrictions, 
where restrictions[i] = [xi, yi] means that person xi and person yi cannot become friends, either directly or indirectly through other people.

Initially, no one is friends with each other. 
You are given a list of friend requests as a 0-indexed 2D integer array requests, where requests[j] = [uj, vj] is a friend request between person uj and person vj.

A friend request is successful if uj and vj can be friends. 
Each friend request is processed in the given order (i.e., requests[j] occurs before requests[j + 1]), and upon a successful request, uj and vj become direct friends for all future friend requests.

Return a boolean array result, where each result[j] is true if the jth friend request is successful or false if it is not.

Note: If uj and vj are already direct friends, the request is still successful.

 

Example 1:

Input: n = 3, restrictions = [[0,1]], requests = [[0,1], [0,2],[2,1]].   -> `0, 1, 2`

parent 0:  1, 2
parent 2:  1


restriction = [[0, 1], [1, 2]], request: [[0,1] [0, 2]]

res:
0: 1 2
1: 2

req:
0: 1

Output: [true,false]
Explanation:
Request 0: Person 0 and person 2 can be friends, so they become direct friends. 
Request 1: Person 2 and person 1 cannot be friends since person 0 and person 1 would be indirect friends (1--2--0).
Example 2:

Input: n = 3, restrictions = [[0,1]], requests = [[1,2],[0,2]]
Output: [true,false]
Explanation:
Request 0: Person 1 and person 2 can be friends, so they become direct friends.
Request 1: Person 0 and person 2 cannot be friends since person 0 and person 1 would be indirect friends (0--2--1).
Example 3:

Input: n = 5, restrictions = [[0,1],[1,2],[2,3]], requests = [[0,4],[1,2],[3,1],[3,4]]
Output: [true,false,true,false]
Explanation:
Request 0: Person 0 and person 4 can be friends, so they become direct friends.
Request 1: Person 1 and person 2 cannot be friends since they are directly restricted.
Request 2: Person 3 and person 1 can be friends, so they become direct friends.
Request 3: Person 3 and person 4 cannot be friends since person 0 and person 1 would be indirect friends (0--4--3--1).
 

Constraints:

2 <= n <= 1000
0 <= restrictions.length <= 1000
restrictions[i].length == 2
0 <= xi, yi <= n - 1
xi != yi
1 <= requests.length <= 1000
requests[j].length == 2
0 <= uj, vj <= n - 1
uj != vj

1. build a restriction map
for each [p1, p2]
restrict[p1].add(p2)
restrict[p2].add(p1)

uf = UF()

for each [r1, r2]
    root1 = uf.find(r1)
    root2 = uf.find(r2)
    if not dfsFindRestrict(root1, root2):
        uf.union(r1, r2)
"""

class UF:
    def __init__(self):
        self._rank = Counter()
        self._parent = defaultdict()
        self._count = 0
        return

    def add(self, data) -> None:
        if self._parent.get(data) is None:
            self._parent[data] = data
            self._count += 1

    def valid(self, data) -> bool:
        return self._parent.get(data) is not None

    def find(self, data):
        if self._parent.get(data) is None:
            raise ValueError(f"data {data} is not added")
        if self._parent.get(data) != data:
            self._parent[data] = self.find(self._parent.get(data))
        return self._parent[data]

    def union(self, data1, data2) -> None:
        data1Root, data2Root = self.find(data1), self.find(data2)
        if data1Root == data2Root:
            return
        if self._rank[data1Root] > self._rank[data2Root]:
            self._parent[data2Root] = data1Root
        elif self._rank[data1Root] < self._rank[data2Root]:
            self._parent[data1Root] = data2Root
        else:
            self._parent[data2Root] = data1Root
            self._rank[data1Root] += 1
        self._count -= 1

    def __len__(self):
        return self._count


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        ans = []
        uf = UF(n)
        for u, v in requests: 
            uu = uf.find(u)
            vv = uf.find(v)
            for x, y in restrictions: 
                xx = uf.find(x)
                yy = uf.find(y)
                if uu == xx and vv == yy or uu == yy and vv == xx: 
                    ans.append(False)
                    break 
                else: 
                    ans.append(True)
                    uf.union(u, v)
        return ans 