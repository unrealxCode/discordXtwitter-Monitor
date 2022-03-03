# discordXtwitter
Python bot that tracks a user Twitter activity and tweets in realtime to search for a discord link and join it asap from the provided discord.


Requirements:

You will need to install the TWINT module to use the code.
You will need to get your discord token and fill it in the code. (line 7)
You will need to get the twitter username of the user you wanna track for the discord link and fill it in the code. (line 39)


Working:

The script will pull all the daily tweets of the user and check for a discord link to join with your provided Discord account.
The script will create a tweets.txt file to keep track of the fetched tweets or older disocrd links from the tweets.
The bot will look for discord links in the user tweets and join the discord if it finds any from the provided discord account.
