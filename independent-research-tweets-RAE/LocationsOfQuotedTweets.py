
import jsonlines

def quotedp(file):
    rite = str(file)+"_places.jsonl"
    with jsonlines.open(rite, mode="w") as writer:
        with jsonlines.open(file) as reader:
            counter = 0
            for tweet in reader:
                t = []
                created = tweet.get('created_at')
                id_str = tweet.get('id_str')
                pl = tweet.get('place')
                t.append(created)
                t.append(id_str)
                t.append(pl)
                writer.write(t)
                counter = counter + 1
                if counter % 1000 == 0:
                    print("Line "+str(counter)+"of Places") 
def quotedu(file):
    rite = str(file)+"_users.jsonl"
    with jsonlines.open(rite, mode="w") as writer:
        with jsonlines.open(file) as reader:
            counter = 0
            for tweet in reader:
                u = []
                pl =tweet.get('place')
                user = tweet.get('user')
                u.append(user)
                u.append(pl)
                writer.write(u)
                counter = counter + 1
                if counter % 1000 == 0:
                    print("Line "+str(counter)+"of Places") 

def quotedm(file):
    rite = str(file)+"_mentions.jsonl"
    with jsonlines.open(rite, mode="w") as writer:
        with jsonlines.open(file) as reader:
            counter = 0
            for tweet in reader:
                created = tweet.get('created_at')
                id_str = tweet.get('id_str')
                mentions = tweet.get('entities',{}).get('user_mentions')
                m = []
                m.append(created)
                m.append(id_str)
                m.append(mentions)
                writer.write(m) 
                counter = counter + 1
                if counter % 1000 == 0:
                    print("Line "+str(counter)+"of Mentions")                
            
def quotedq(file):    
    rite = str(file)+"_quotes.jsonl"
    with jsonlines.open(rite, mode="w") as writer:
        with jsonlines.open(file) as reader:
            counter = 0
            for tweet in reader:
                created = tweet.get('created_at')
                id_str = tweet.get('id_str')
                quotes = tweet.get('quoted_status')
                q = []
                q.append(created)
                q.append(id_str)
                q.append(quotes)
                writer.write(q)         
                counter = counter + 1
                if counter % 1000 == 0:
                    print("Line "+str(counter)+"of Quoted")  
def quotedr(file):                
    rite = str(file)+"_replies.jsonl"
    with jsonlines.open(rite, mode="w") as writer:
        with jsonlines.open(file) as reader:
            counter = 0
            for tweet in reader:
                created = tweet.get('created_at')
                id_str = tweet.get('id_str')
                reply_s_id = tweet.get('in_reply_to_status_id_str')
                reply_u_id = tweet.get('in_reply_to_user_id_str')
                r = []
                r.append(created)
                r.append(id_str)
                r.append(reply_s_id)
                r.append(reply_u_id)
                writer.write(r)         
                counter = counter + 1
                if counter % 1000 == 0:
                    print("Line "+str(counter)+"of Replied")
    return

# quotedp("AllQuotedTweets_alone.jsonl")
quotedu("AllQuotedTweets_alone.jsonl")
quotedm("AllQuotedTweets_alone.jsonl")
quotedq("AllQuotedTweets_alone.jsonl")
quotedr("AllQuotedTweets_alone.jsonl")      
                
                
                    
                
                
                