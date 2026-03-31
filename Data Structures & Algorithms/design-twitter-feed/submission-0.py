import heapq
import time
from typing import List

class Twitter:

    def __init__(self):
        self.tweet_map = {}  # userId -> list of (timestamp, tweetId)
        self.follower_followee_map = {}  # followerId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet_map:
            self.tweet_map[userId] = []
        # Use negative timestamp for max-heap behavior with min-heap
        self.tweet_map[userId].append((-time.time(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # If user has no follow list, treat as empty
        followees = self.follower_followee_map.get(userId, set())

        # Include user's own tweets
        users_to_collect = set(followees)
        users_to_collect.add(userId)

        minheap = []

        # Collect tweets
        for user in users_to_collect:
            if user in self.tweet_map:
                for t in self.tweet_map[user]:
                    heapq.heappush(minheap, t)

        # Get the 10 most recent tweets
        res = []
        for _ in range(10):
            if not minheap:
                break
            _, tweet_id = heapq.heappop(minheap)
            res.append(tweet_id)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower_followee_map:
            self.follower_followee_map[followerId] = set()
        if followeeId != followerId:  # Prevent self-follow
            self.follower_followee_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower_followee_map:
            self.follower_followee_map[followerId].discard(followeeId)
