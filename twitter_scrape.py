import tweepy
import os
import requests
from random import randrange
from keys import *


def scrape_images(screen_name):
    auth = tweepy.OAuthHandler(TWITTER_API, TWITTER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    auth.secure = True

    api = tweepy.API(auth)

    alltweets = []
    new_tweets = api.user_timeline(screen_name=screen_name, count=1)
    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        new_tweets = api.user_timeline(
            screen_name=screen_name, count=500, max_id=oldest
        )
        alltweets.extend(new_tweets)

        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    outtweets = []
    for tweet in alltweets:
        try:
            print(tweet.entities["media"][0]["media_url"])
        except (NameError, KeyError):
            pass
        else:
            outtweets.append(tweet.entities["media"][0]["media_url"])

    for src in outtweets:
        response = requests.get(src)
        if response.status_code == 200:
            name = random_number() + ".jpg"
            path = os.path.join(save_path, name)
            with open(path, "wb+") as f:
                f.write(response.content)
            print(
                "downloading from @{},  filename: {} downloaded".format(
                    screen_name, name
                )
            )
        else:
            print("erorr occurred")
            continue


def random_number():
    return str(randrange(1000000))


if __name__ == "__main__":
    cultural = [
        "ATBWomen",
        "WW2Facts",
        "HarariMelesay",
    ]
    punkRock = ["PunkRockStory"]
    architecture = ["arab11__", "MonochromeMis", "1by1work"]

    goHard = [
        "WallpaperHQ1",
        "isthatkap",
        "fightpicsgohard",
        "f1_hardpics",
        "cycIingpics",
        "HardWrestlePics",
        "boxing_history",
    ]
    artwork = [
        "ArtOrthodox",
    ]

    save_path = "/Users/damolaolugboji/Desktop/code/Image Scrape/goHard"

    for account in goHard:
        scrape_images(account)

