from tiktok_bot import TikTokBot
import csv
import datetime
from colorama import Fore, Back, Style
import os
import json
import utils 
import constant

hashtags = dict()

try:
    os.mkdir(constant.DATA_DIR)
except OSError as e:
    print("Directory exists")

bot = TikTokBot()

my_feed = bot.list_for_you_feed(constant.POST_TO_FETCH)

print(Fore.CYAN + str(len(my_feed)), Fore.RED + "posts found")
print(Style.RESET_ALL)

popular_posts = [
    post for post in my_feed if post.statistics.play_count > constant.PLAYS_MIN]

print(Fore.CYAN + str(len(popular_posts)), Fore.RED + "popular posts found")
print(Style.RESET_ALL)

fieldnames = ['User ID', 'URL', 'Description', 'Comments', 'Likes']

with open(utils.buildFileName("_plays", 'csv'), mode='a') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    utils.writeCsvAndFilterHashtags(popular_posts, hashtags, writer)

most_liked_posts = [
    post for post in my_feed if post.statistics.digg_count > constant.LIKE_MIN]

print(Fore.CYAN + str(len(most_liked_posts)), Fore.RED + "toplike posts found")
print(Style.RESET_ALL)

with open(utils.buildFileName("_likes", 'csv'), mode='a') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    utils.writeCsvAndFilterHashtags(popular_posts, hashtags, writer)


most_shared_posts = [
    post for post in my_feed if post.statistics.share_count > constant.SHARE_MIN]

print(Fore.CYAN + str(len(most_shared_posts)),
      Fore.RED + "topshare posts found")
print(Style.RESET_ALL)

with open(utils.buildFileName("_shares", 'csv'), mode='a') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    utils.writeCsvAndFilterHashtags(popular_posts, hashtags, writer)
