import datetime
import constant
import json
import re


def getData():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def buildFileName(name, ext):
    return (constant.DATA_DIR) + getData() + (name) + "." + ext


def writeCsvAndFilterHashtags(popular_posts, hashtags, writer):
    hashtagregex = re.compile(r"#(\w+)")
    for post in popular_posts:
        print(str(post.author_user_id), str(post.share_url), str(post.desc),
              post.statistics.comment_count, post.statistics.digg_count)
        writer.writerow({'User ID': str(post.author_user_id), 'URL': str(post.share_url), 'Description': str(
            post.desc), 'Comments': post.statistics.comment_count, 'Likes': post.statistics.digg_count})

        posttags = hashtagregex.findall(str(post.desc))
        new_hashtags = hashtagCounter(posttags, hashtags)
        saveHashtag(new_hashtags)


def hashtagCounter(posttags, hashtags):
    for tag in posttags:
        if tag in hashtags:
            hashtags[tag] += 1
        else:
            hashtags[tag] = 1
    return hashtags


def saveHashtag(hashtags):
    with open((constant.DATA_DIR + "hashtags.json"), 'w') as fout:
        json.dump(hashtags, fout)
