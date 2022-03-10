class User:  # first letter should be capital
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # not passed in the main line, so default followers are 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1 # self following or followers, take from original and adds one if someone defines that
        # function
        # this self helps put everything in the new objects created.
        print("new user being called")

    # init function called everytime added a new attribute
    # add as many parameters in the init function
    pass


user_1 = User("001", "Karat")

print(user_1.username)

# constructor
