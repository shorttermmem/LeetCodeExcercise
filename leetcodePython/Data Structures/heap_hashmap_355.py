#https://leetcode.com/problems/design-twitter/description/
# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]
from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.count=0 # This is a instance level counter used to timestamp tweets, 0 is the oldest for minheap
        self.following=defaultdict(set) # Using a set ensures no duplicate followees and O(1) lookup/removal.
        self.post=defaultdict(list) # value is a list of [count, tweetId] pairs

    # Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post[userId].append([self.count, tweetId])
        self.count -= 1

    # Retrieves the 10 most recent tweet IDs in the user's own news feed or from their followees.
    # ordered from most recent to least recent 
    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId) # make sure to show user's own feeds
        minheap = []
        for followee in self.following[userId]:
            i = len(self.post[followee]) - 1 # followee's most recent tweet
            if i >= 0:
                count, tweetId = self.post[followee][i] # get followees tweet
                minheap.append([count,tweetId,followee,i]) # save for most recent lookup later
        heapq.heapify(minheap)

        res = []

        while minheap and len(res) < 10:
            count,tweetId,followee,i = heapq.heappop(minheap) # get the most recent tweet
            res.append(tweetId)
            if i > 0:
                count, tweetId = self.post[followee][i - 1] # add another tweet from the same followee
                heapq.heappush(minheap, [count,tweetId,followee,i-1])
        return res
        
    # The user with ID followerId started following the user with ID followeeId.
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)