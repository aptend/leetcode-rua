from typing import List
from collections import defaultdict
from itertools import count


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follow_table = defaultdict(set)
        self.posts = defaultdict(list)
        self.gid = count()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.posts[userId].append((next(self.gid), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tws = self.posts[userId][:]
        for f in self.follow_table[userId]:
            tws.extend(self.posts[f][-10:])
        return [p[1] for p in sorted(tws, reverse=True)[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follow_table[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follow_table[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)"


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

def main():
    twitter = Twitter()
    operations = ['postTweet', 'getNewsFeed', 'follow',
                  'postTweet', 'getNewsFeed', 'unfollow', 'getNewsFeed']
    oprands = [[1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    for opt, opd in zip(operations, oprands):
        if hasattr(twitter, opt):
            print(getattr(twitter, opt).__call__(*opd))


if __name__ == '__main__':
    main()
