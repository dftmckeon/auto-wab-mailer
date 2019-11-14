import praw

class RedditFetch:
    def __init__(self):
        self.reddit = praw.Reddit(client_id='BtSNIZ8esgXqug',
                            client_secret='vQbjL0ZCa12xMEHuwWHNQ5KsP3g',
                            user_agent='Python:Auto-WAB-Mailer:Version-1.0 (by /u/dftmckeon)',
                            username='dftmckeon',
                            password='EmeraldWhale.99')

    def hot_post(self, subreddit, post_number):
        submissions = []
        for submission in self.reddit.subreddit(subreddit).hot(limit=post_number):
            submissions.append(submission.title)
            
        return submissions[-1]