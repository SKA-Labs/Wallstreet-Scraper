import praw

reddit = praw.Reddit(
    client_id="mmsRASRxa0gxzP-QgYi_-g",
    client_secret="G96kL_fpLHwFCJ-PbCaEvWyHB0ZlOg",
    user_agent="User-Agent: macos:RedditScraper:v1.0 (by /u/x4la)",
    password="AlexS123",
    username="x4la",
)

count=0
for submission in reddit.subreddit("leagueoflegends").top(limit=10):
    if "a" in submission.title:
        count+=1
    print(submission.title)
    print(submission.selftext)

print(count)
