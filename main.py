import twint
import re
import requests
import time


auth = ""

previous_links = []


def clear_link(link):
    ## removing the https and all that stuff and getting the main code
    cle_link = ''.join(e for e in link if e.isalnum())
    return cle_link[14:]


def join_server(code):
    invite = code
    header = {
        "authorization": auth}
    try:
        r = requests.post(f"https://discord.com/api/v8/invites/{invite}", headers=header)
        print('*'*100)
        print("Join the Server u can now rest")
        print(r)
        print(r.status_code)
        print('*'*100)
    except:
        print('*'*100)
        print("didn't join")
        print('*'*100)


# Configure
c = twint.Config()
## Type the username of the account without including the @

c.Username = ""

c.Output = 'tweets.txt'
while True:
    try:
        with open('tweets.txt', 'r', encoding="utf8") as file:
            data = file.read()
            if data:
                tweets = data.split('\n')
                for tweet in tweets:
                    ## finding links from tweets
                    links = re.findall(r'(https?://[^\s]+)', tweet)
                    if links:
                        for link in links:
                            ## converting the t.co into discord link
                            try:
                                resp = requests.head(link)
                                server_join = resp.headers["Location"]
                            except:
                                continue       
                            ## checking if that link is discord invite link or not                     
                            if 'discord.gg' in server_join:
                                if (server_join in previous_links) == False:
                                    ## joining the server
                                    join_server(clear_link(server_join))
                                    print(server_join)
                                previous_links.append(server_join)

                open('tweets.txt', 'w').close()
            else:
                twint.run.Search(c)
            time.sleep(5)
    except:
        pass
        time.sleep(10)
