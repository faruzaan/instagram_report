from datetime import datetime
from itertools import dropwhile, takewhile
import calendar

import instaloader

def findDay(date):
    year, month, day= (int(i) for i in date.split('-'))   
    dayNumber = calendar.weekday(year, month, day)
    days =["Senin", "Selasa", "Rabu", "Kamis",
                         "Jumat", "Sabtu", "Minggu"]
    return (days[dayNumber])

L = instaloader.Instaloader()
username = "530jakarta"

posts = instaloader.Profile.from_username(L.context, username).get_posts()

UNTIL = datetime(2022, 11, 30)
SINCE = datetime(2022, 12, 31)

like_post = []
post_datetime = []

for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
    like_post.append(post.likes) 
    post_datetime.append(post)

print(post_datetime)
posts_sorted_by_likes = sorted(post_datetime,key=lambda p: p.likes + p.comments, reverse=True)
print(posts_sorted_by_likes)

count = 0
for index, post in enumerate(posts_sorted_by_likes, 1):
  # L.download_post(post, target=f"{username}_top_{index}")
  date = str(post.date)
  l = len(date)
  remove_hour = date[:l-9]
  print(findDay(remove_hour))
  count += 1
  if count == 3:
    break






