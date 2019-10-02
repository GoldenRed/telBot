# telBot
Repo for my telegram bot(s)

## Todo:
[x] - UMD_SB_BOT

[ ] - EriAssistBot

[ ] - EfremFamBot

## Deployment

The idea is that they will live on my Raspberry Pi, since the workload isn't that high and there's no need to expose their IP addresses to the public.

# List of Bots:

## UMD_SB_Bot:

Based on my HH4R Bot. Communicates with the same API to give you a list of the closest stations. It can also deal with quite a few corner cases.

rpi3 branch: to run script in background do
nohup /home/pi/telBot/scripts/startTelBots.sh &>/dev/null

## EriAssistBot

I noticed that it's possible for people in Eritra to get (relatively) good connectivity to users on Telegram, much more than what they could get with other parts of the Internet. My idea is then to create a bot that can serve info by scraping or calling on APIs and packaging that into a lightweight Telegarm text message. Stuff like:

[ ] - /airport for Asmara airport info regarding arrivals/departures
[ ] - /current for information on currency exchange, requested by my cousin
[ ] - /wiki for requests to wikipedia on topics; e.g. you could get the article summaries or maybe the bot would serve a keyboard with various aspects of the article

... and so on.

## EfremFamBot:

Will be chilling in the family Telegram group, ready to do stuff like:

[ ] - Congratulate people on their birthdays
[ ] - Send reminders to us
[ ] - Serve images, either on request or randomly or some other way
