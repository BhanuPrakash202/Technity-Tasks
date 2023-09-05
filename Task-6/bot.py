import csv
import json
import requests
import telebot

with open("Movies.csv", mode="w") as csvfile:
    info = ["Title", "Year", "Genre", "Plot"]
    write = csv.DictWriter(csvfile, fieldnames=info)
    write.writeheader()
csvfile.close()
# TODO: 1.1 Get your environment variables
bot_id = '6046404987:AAEEc8dFOwbRQ6o-U0S3mpS9AdSDMbnVmC8'

bot = telebot.TeleBot(bot_id)


@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')


@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message,
                 '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    # TODO: 1.2 Get movie information from the API
    # http://www.omdbapi.com/?i=tt3896198&apikey=4e01bc39
    yourkey = "4e01bc39"
    name = message.text.split()[1:]
    fname = "+".join(name)
    link = 'http://www.omdbapi.com/?t=' + fname + '&apikey=' + yourkey
    req = requests.get(link)
    data = json.loads(req.text)
    if data['Response'] == "True":
        title = data['Title']
        year = data['Year']
        genre = data['Genre']
        plot = data['Plot']
        picurl = data['Poster']
        # TODO: 1.3 Show the movie information in the chat window
        bot.send_photo(message.chat.id, picurl,
                       caption=f"Title : {title}\nYear : {year}\nGenre : {genre}\nPlot : {plot}")
        # TODO: 2.1 Create a CSV file and dump the movie information in it
        with open("Movies.csv", mode="a") as csvfile1:
            writer = csv.writer(csvfile1)
            writer.writerow([title, year, genre, plot])
        csvfile.close()
    else:
        bot.send_message(message.chat.id, "Sorry,we couldn't find the requested movie")


@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    # TODO: 2.2 Send downlodable CSV file to telegram chat
    with open("Movies.csv", mode="rb") as csvfile2:
        bot.send_document(message.chat.id, csvfile2)
    csvfile2.close()


@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand ' + '\N{confused face}')


bot.infinity_polling()
