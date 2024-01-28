from api import ApiHandler
from config import ConfigHandler
from faker import Faker


class DataGenerator:
    def __init__(self):
        self.fake = Faker()
        self.config_handler = ConfigHandler()
        self.api_handler = ApiHandler()
        self.users_tokens = []
        self.posts_ids = []
        self.likes = 0

    def generate_users(self):
        """Users registration through API requests."""
        number_of_users = int(
            self.config_handler.get_option("default", "number_of_users", "5")
        )
        for _ in range(number_of_users):
            profile = self.fake.profile()
            password = self.fake.unique.pystr()
            token = self.api_handler.signup(
                profile["mail"], profile["username"], password
            )
            self.users_tokens.append(token)
        print(f"Created {number_of_users} users!")

    def generate_posts(self):
        """Posts generation through API requests."""
        max_posts_per_user = int(
            self.config_handler.get_option("default", "max_posts_per_user", "5")
        )

        for user_token in self.users_tokens:
            for _ in range(self.fake.random_int(min=1, max=max_posts_per_user)):
                title = " ".join(self.fake.words(nb=5))
                content = self.fake.paragraph(nb_sentences=5)

                post_id = self.api_handler.create_post(title, content, user_token)
                self.posts_ids.append(post_id)
        print(f"Created {len(self.posts_ids)} posts!")

    def generate_likes(self):
        """Likes generation through API requests."""
        max_likes_per_user = int(
            self.config_handler.get_option("default", "max_likes_per_user", "5")
        )
        for user_token in self.users_tokens:
            if max_likes_per_user >= len(self.posts_ids):
                posts_to_like = self.posts_ids
            else:
                posts_to_like = self.fake.random_elements(
                    elements=self.posts_ids,
                    length=self.fake.random_int(min=1, max=max_likes_per_user),
                    unique=True,
                )
            for post_id in posts_to_like:
                self.api_handler.like_post(post_id, user_token)
                self.likes += 1
        print(f"Created {self.likes} likes!")
