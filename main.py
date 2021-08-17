import twint
from datetime import datetime

hashtags = ["#twlz", "#twitterlehrerzimmer"]

print(f"Start at {datetime.now()}")

for hashtag in hashtags:
    c = twint.Config()
    c.Search = hashtag
    c.Hide_output = True
    c.Pandas = True
    start_running_search = datetime.now()
    twint.run.Search(c)
    end_running_search = datetime.now()

    filename = f"tweets_{hashtag}"

    tweets_df = twint.storage.panda.Tweets_df
    try:
        tweets_df.to_csv(filename + ".csv")
        tweets_df.to_excel(filename + ".xlsx")
    except Exception as e:
        print(e)

    print(f"Done {hashtag}, took {end_running_search-start_running_search}")

