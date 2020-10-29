import praw
import time

# Made by @cultureduh

try:
    reddit = praw.Reddit(client_id='lieRFMknY12JWw', client_secret='o7jSLDovD5Ub11M8TWpfSGhQEXE',
                         username='FreeKrma4You', password='freekrma4you',
                         user_agent='User-Agent:<console:FreeKrma4You:1.12')
except Exception as e:
    print("#Login failed.", e)


try:
    open('postid.txt', 'r')
except FileNotFoundError:
    open('postid.txt', 'w')


# Check if the submission id is in the postid list.
def postidcheck(postid):
    postidlist = open('postid.txt', 'r+').read().split('\n')
    for post in postidlist:
        if postid == post:
            return post
            break

sublist = ["AsianPornIn1Minute", "AsianHottiesGIFS","asianbabes","The_Best_NSFW_GIFS","NSFW_Cams","Instagrammodels","Pornstarsnow","O_Faces",
"hotclub","FakeTitsWorship","Megalinksfree","LEAKEDonlyfans","SexyTummies","MariaGjieli157","KattLeyaAndStrellaKat","NSFW_Amazing","HottiesHub","desnudas","AmateurWhores","packs_porno_gratis"
,"NSFWRare","TwerkStop","Piabunny","LadyLebraa","AvalonHopee","cs_blondebombshell","laceykingxo","Jhenerosetv","Wife2share","wifeporn","PacksLatinas","WifeSwapping","YOUNGPRETTYHOES2","Whopperme","boobs","Slut"]  # Subreddit list to crosspost to.
privatesub = 'TikToknOnlyFans'  # Subreddit to crosspost from.
privatesub = reddit.subreddit(privatesub)

while True:
    for submission in privatesub.new(limit=None):
        if submission.id == postidcheck(submission.id):  # Check if the submission has already been crossposted.
            continue
        for sub in sublist:  # Go through each each subreddit in the sublist.
            try:
                submission.crosspost(sub)  # Crosspost the submission in the current subreddit.
                open('postid.txt', 'a+').write(f'{submission.id}\n')  # Add the submission's id to the list.
            except Exception as e:
                print(e)
            time.sleep(300)  # 10 minutes cooldown due to reddit's ratelimit.
