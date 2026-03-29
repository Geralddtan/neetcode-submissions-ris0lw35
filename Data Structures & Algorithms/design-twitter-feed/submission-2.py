class Twitter:
    def __init__(self):
        self.tweet_map = defaultdict(list)
        self.follower_map = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []
        self.follower_map[userId].add(userId)
        for followee_id in self.follower_map[userId]:
            if followee_id in self.tweet_map:
                index = len(self.tweet_map[followee_id]) - 1
                count, tweetId = self.tweet_map[followee_id][index]
                maxHeap.append([count, tweetId, followee_id, index-1])

        heapq.heapify(maxHeap)
        while maxHeap and len(res) < 10:
            count, tweetId, followee_id, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet_map[followee_id][index]
                heapq.heappush(maxHeap, [count, tweetId, followee_id, index-1])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_map[followerId]:
            self.follower_map[followerId].remove(followeeId)
