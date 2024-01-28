from utils import DataGenerator


def do_hacking():
    data_generator = DataGenerator()
    data_generator.generate_users()
    data_generator.generate_posts()
    data_generator.generate_likes()


if __name__ == "__main__":
    do_hacking()
