import time
class Twitter:

    def __init__(self):
        self.i=0
        self.user_tweets = defaultdict(list)
        self.follower_to_followee = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.i+=1
        self.user_tweets[userId].append((self.i, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        temp = []
        users = [userId] + self.follower_to_followee[userId]
        for follower in users:
            curr_tweets = self.user_tweets[follower]
            for i in range(len(curr_tweets)-1, max(len(curr_tweets)-11, -1), -1):
                d = curr_tweets[i]
                temp.append(d)
        heapq.heapify(temp)
        tweets = []
        while len(temp)>10:
            heapq.heappop(temp)
        # print("temp", temp)
        while temp:
            d = heapq.heappop(temp)

            tweets.append(d[1])
            
        return tweets[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId and followeeId not in self.follower_to_followee[followerId]:
            self.follower_to_followee[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId and followeeId in self.follower_to_followee[followerId]:
            self.follower_to_followee[followerId].remove(followeeId)
