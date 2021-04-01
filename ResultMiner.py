class TweetMiner():

    def __init__(self, api, tweet_limit):
        
        self.api = api
        self.tweet_limit = tweet_limit
        
        
    def retrieve_data(self, tag, WOE_ID, page_limit):
        
        cleaned_data = []
        
        for i in range(page_limit):         
            tweet_id = False
            
            url = "q=twitter%20"+tag+"&result_type=recent&count=500"
            data = self.api.GetSearch(raw_query=url)
            statuses = [status.AsDict() for status in data]
        
            for status in statuses:
            
                if status['lang'] == "en":
                    try:
                        data = {
                            'id' : status['id'],
                            'hashtag': tag,
                            'created_at' : status['created_at'],
                            'tweet' : status['text'],
                            'user_name' : status['user']['screen_name'],
                            'retweet_count' : status['retweet_count'],
                        }
                
                    except: 
                        data = {
                            'id' : status['id'],
                            'hashtag': tag,
                            'created_at' : status['created_at'],
                            'tweet' : status['text'],
                            'user_name' : status['user']['screen_name'],
                            'retweet_count' : 0,
                        }
                        cleaned_data.append(data)
                        
        return cleaned_data