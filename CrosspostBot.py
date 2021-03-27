# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:09:31 2020

@author: chris
"""

import praw
import time

# Made by @cultureduh

try:
    reddit = praw.Reddit(client_id='ZVBwHNapCLhh-A', client_secret='mLVl9xg78Bc39r-RRoFwoL1q524mcQ',
                         username='ok-overlay', password='chindi12',
                         user_agent='User-Agent:<console:ok-overly:1.0')
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

sublist = ["ALEXASMORGANNN","AllAdultNSFW",
           "allBustyBabes","AmandaNicole",
           "Amateur_Bitches","AmateurSlutWives","AmateurWhores",
           "arabsgonewild","BaddestGirls",
           "Bestcamnudes","BigTiddieGothGirls","BigTitModels",
           "BItedSizeSexy","BonerAlert",
           "Boners4Life","boobs","BoobsBetweenArms",
           "BoobsInYourFace","Booty_lovers","BrasOnTitsOut","brunette","Chaturbatevideos",
           "CherryBarbie","CuteGirlPorn","Dabofkya_GOAT","DeliciousnessXXX","desnudas","Pounding_Hard",
           "TikTokNudity","TikTokNude","Dildo_Gifs","DirtySocialMedia",
           "elizabethannepelayo","FakeTitsWorship","freeusefamily","FuckThatsHot",
           "GolemSexy","HipsterGirlsNSFW",
           "InterracialBreeding","JasmineBanks","KattLeyaAndStrellaKat","Katvong",
           "knockmeup","laceykingxo","LadyLebraa","lizzywurstonlyfans"
           "MarissaDaNae","Megaz4Free","Nategotkeys",
           "naughtyNerdGirls","NSFW_Uncensored","NSFWexchange","NSFWPublic","NSFWRare",
           "PornWorlds","PussyAssTitsLover","shavedpussies",
           "Slutsofonlyfans","Splitview","SuzyCortez","TikTokNudes",
           "Teenpussyx","TheGoatOfXXX","TheTylerCamile","toveyahfans",
           "ThotNetwork","TikThots","MegalinkNSFW",
           "TwerkStop","undertable_porn","wetspot","Wife2share"
           "wifeporn","WifeSwapping","youngporn","YOUNGPRETTYHOES2","ZaylaSkye","Slut"] # Subreddit list to crosspost to.

privatesub = 'PacksFree'  # Subreddit to crosspost from.
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
            time.sleep(660)  # 5 minutes cooldown due to reddit's ratelimit.
               


















