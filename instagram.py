import instaloader
import pandas as pd
from PIL import Image
import os
import PIL
import glob

bot = instaloader.Instaloader()
# bot.login(user="aing_mauung", passwd="27farhan")

profile = instaloader.Profile.from_username(bot.context, 'euro_cycle_scbd')

posts = profile.get_posts()
count = 0
for index, post in enumerate(posts, 1):
  bot.download_post(post, target=f"{profile.username}_{index}")
  count += 1
  if count == 3:
    break

# for index in enumerate(1):
  # image = Image.open("{euro_cycle_scbd}_{index}/")
# print(profile)