# a class to add the functionality of liking posts and keeping a track of who has
# liked a post.
class Likes:
    def __init__(self):
        self.likes = 0
        self.user_likes = []

    def update_likes(self):
        self.likes

    def likes(self):
        self.likes += 1
        self.update_likes()

    def update_user_likes(self):
        self.user_likes

    def user_likes(self, user):
        self.user_likes.append(user)
        self.update_user_likes()