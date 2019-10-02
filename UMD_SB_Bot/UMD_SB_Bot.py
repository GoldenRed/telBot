from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, requests, json

with open('../../dev/UMD_SB_Bot.txt') as f:
    API_TOKEN = f.read()

updater = Updater(token=API_TOKEN, use_context=True)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='/home/pi/telBot/UMD_SB_Bot/UMD_SB.log', filemode='a', level=logging.INFO)

logger = logging.getLogger(__name__)

state = 0

def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def start(update, context):
    global state 
    state = 1
    context.bot.send_message(chat_id=update.message.chat_id, text="Hi Rewina! Start sending me addresses. Send /quit to stop.")

def quit(update, context):
    global state 
    if state == 1:
        state = 0
        context.bot.send_message(chat_id=update.message.chat_id, text="Okay, I'm stopping now.")
    elif state == 0:
        context.bot.send_message(chat_id=update.message.chat_id, text="I'm not even on right now...")

def normal(update, context):
    if state == 0:
        context.bot.send_message(chat_id=update.message.chat_id, text="Write /start to begin checking addresses!")

    elif state == 1:
        logger.info("Searched for address: %s",  update.message.text)
        url = "http://hh4rapi-env.6gsmdkiciw.us-east-2.elasticbeanstalk.com/json/{}/10".format(update.message.text)
        res = requests.get(url)
        if res.ok:
            jData = json.loads(res.content.decode('utf-8'))
            reply_vec = []
            for stat in jData:
                if stat != 'QUERY_INFO': #QUERY_INFO is the query's own GPS coordinates
                    reply = "Station: {} {}, distance {} km.".format(stat, jData[stat][0]['buss_fullLineID'][0], jData[stat][0]['distance'])
                    dist = int(jData[stat][0]['distance'])
                    reply_vec.append([reply, dist])
            reply_vec.sort(key=lambda x: x[1]) #We sort the stations in accordance to distance
            for elem in reply_vec: #print them out in order of closest station first
                context.bot.send_message(chat_id=update.message.chat_id, text=elem[0])                
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text="Failed to return stations. Tip: Try adding \"Maryland\" to your address.")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Error: Weird State.")


    


if __name__ == '__main__':
    start_handler = CommandHandler('start', start)
    normal_handler = MessageHandler(Filters.text, normal)
    quit_handler = CommandHandler('quit', quit)
    unknown_handler = MessageHandler(Filters.command, unknown)

 
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(normal_handler)
    updater.dispatcher.add_handler(quit_handler)
    updater.dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()
