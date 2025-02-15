import collections
import heapq
"""
multiple pointers + minHeap + set
time:
    postTweet: O(1)
    getNewsFeed: O(k), k = number of followees of the userId
    follow: O(1)
    unfollow: O(1)
space:
    O(n): number of function calls
    getNewsFeed: O(k)
"""

class Twitter:

    def __init__(self):
        self.user_tweets = {}
        self.following_dict = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_tweets:
            self.user_tweets[userId] = collections.deque([])

        self.user_tweets[userId].append((self.count, tweetId))
        if len(self.user_tweets[userId]) > 10:
            self.user_tweets[userId].popleft()
        
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        results = []
        minHeap = []
        # make sure to check if the userId has any followers
        if userId not in self.following_dict:
            self.following_dict[userId] = set()
        
        self.following_dict[userId].add(userId)

        for curUser in self.following_dict[userId]:
            # check if curUser has any posts at all
            if curUser in self.user_tweets:
                index = len(self.user_tweets[curUser]) - 1
                curCount, curTweet = self.user_tweets[curUser][index]
                minHeap.append([curCount, curUser, curTweet, index - 1])
        
        heapq.heapify(minHeap)

        while len(minHeap) > 0 and len(results) < 10:
            curCount, curUser, curTweet, curIndex = heapq.heappop(minHeap)
            results.append(curTweet)
            
            if curIndex >= 0:
                nextCount, nextTweet = self.user_tweets[curUser][curIndex]
                heapq.heappush(minHeap, [nextCount, curUser, nextTweet, curIndex - 1])

        return results

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following_dict:
            self.following_dict[followerId] = set()
        
        self.following_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following_dict:
            if followeeId in self.following_dict[followerId]:
                self.following_dict[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

"""
init:
user_tweets = {userId : queue[(time, tweetId)]}
following_dict = {followerId : set[followeeIds]}
count = 0

postTweet:
update user_tweets with userId with (count, tweetId)
if the userId's tweets size > 10 -> pop the first element out of queue
count -= 1

follow:
update following_dict accordingly

unfollow:
check if the following relationship exists
update follow_dict accordingly

getNewsFeed: 
# use the fact that the later tweet's in a userId's queue would be more recent
results = []
go through all of the userId's followeeIds and also the userId itself:
    update minHeap with [time, followeeId, tweetId, nextIndex]

heapify

while minHeap is not empty and result's size < 10:
    pop minHeap element and add tweetId into results
    find next most recent tweet of the followeeId using nextIndex of popped element
    update minHeap with [time, followeeId, tweetId, nextIndex - 1]

k = number of followees of the userId
O(10k)
"""
