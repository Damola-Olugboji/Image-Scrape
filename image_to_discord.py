import os
import discord
import asyncio
import cv2
from keys import *


client = discord.Client()
CHANNEL_ID = 982861888150970410


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):

    if message.content.startswith("$hello"):
        await message.channel.send("Hello Motherfucker")


# client.run(DISCORD_TOKEN)


def get_images():
    def _get_caption(path):
        file = open(path, "r")
        lines = file.read()
        print(lines.split("\n", 1)[0])
        file.close()
        return lines.split("\n", 1)[0]

    image_dict = {}
    cwd = "/Users/damolaolugboji/Desktop/code/Image Scrape/InstagramScrape"
    folders = [
        folder
        for folder in os.listdir(cwd)
        if os.path.isdir(os.path.join(cwd, folder)) is True
    ]
    counter = 0
    for folder in folders:
        image_list = [
            file for file in os.listdir(os.path.join(cwd, folder)) if file[-3:] == "jpg"
        ]
        for image in image_list:
            try:
                image_path = os.path.join(cwd, folder, image)
                caption_path = os.path.join(cwd, folder, image[:-3] + "txt")
                caption = _get_caption(caption_path)
                # print(image_path, caption_path)
                loaded_image = cv2.imread(image_path)
                RGB_img = cv2.cvtColor(loaded_image, cv2.COLOR_BGR2RGB)
                image_dict[str(counter)] = [RGB_img, caption]

            except:
                continue


get_images()


def clean_folders():
    cwd = "/Users/damolaolugboji/Desktop/code/Image Scrape/InstagramScrape"
    extensions = ["jpg", "txt"]
    folders = [
        folder
        for folder in os.listdir(cwd)
        if os.path.isdir(os.path.join(cwd, folder)) is True
    ]
    for folder in folders:
        files = [
            file
            for file in os.listdir(os.path.join(cwd, folder))
            if file[-3:] not in extensions
        ]
        for file in files:
            os.remove(os.path.join(cwd, folder, file))

