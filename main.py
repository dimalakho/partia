import telebot
from telebot import types
import datetime

f = open("token.txt", "r")
bot = telebot.TeleBot(f.readline())
f.close()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👏 Хочу в партию!")
    btn2 = types.KeyboardButton("📕 Хочу ознакомиться с Уставом Партии!")
    btn3 = types.KeyboardButton("🪶 Хочу узнать историю Партии!")
    btn4 = types.KeyboardButton("🪪 Хочу посмотреть на партбилет!")
    markup.add(btn1, btn2, btn3, btn4)
    img1 = open('img1.png', 'rb')
    bot.send_photo(message.chat.id, img1)
    bot.send_message(message.chat.id,
                     text='*Здравствуй, товарищ!* Тебя приветствует партийный бот! Чтобы вступить в Партию, нажми в меню снизу!'.format(
                         message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👏 Хочу в партию!':
        bot.send_message(message.chat.id,
                         text='*Чтобы вступить в Партию, напишите слово "ПАРТИЯ" в личные сообщения одному из генсеков:*                                                                                    '
                              '✅ Шакарян Николай – @shakaryannikolay                                                                                                   '
                              '✅ Власов Георгий – @divanniyphilosopher                                                                                               '
                              '✅ Родин Ефим – @Facolaco                                                                                                         '
                              '✅ Манихин Всеволод – @sevamanikhin                                                                                                  '
                              '✅ Белоусов Тимофей – @got_timmed                                                                                                   '.format(
                             message.from_user))
        print(message.from_user.username, datetime.datetime.now())
    if message.text == '📕 Хочу ознакомиться с Уставом Партии!':
        bot.send_message(message.chat.id,
                         text='*Новейшая редакция Устава доступная по этой ссылке:* https://docs.google.com/document/d/1J-FLqRM_xQELqp37D91gnBOEUY3jazgyjQxFEPHyXzs/edit?usp=sharing.'.format(
                             message.from_user))
        print(message.from_user.username, datetime.datetime.now())
    if message.text == '🪶 Хочу узнать историю Партии!':
        img2 = open('img2.png', 'rb')
        bot.send_photo(message.chat.id, img2)
        bot.send_message(message.chat.id,
                         text="В один из прохладных осенних деньков, а именно 20 сентября 2022 года, четырьмя Генсеками была создана политическая партия. И назвали они её довольно остроумно: ПАРТИЯ.                                                                                                            "
                              "Одна из главных особенностей партии – абсолютный политический плюрализм. Учитываются абсолютно все точки зрения, приветствуются любые идеи и идеологии, которые не нарушают закон.                                                                                                             "
                              "Первыми членами партии стали одноклассники генсеков. Их привлекла харизма и обаятельность Генсеков, а также простота вступления в партию.                                                                                                             "
                              "Уже осенью ПАРТИЯ обзавелась своим интернационалом: открылось представительство в Германии (председателем немецкого отделения является Денисов Арсений, бывший ученик лицея).                                                                                                             "
                              "Примерно тогда же Георгием и Николаем был написан Устав, который отражает основные принципы, по которым действует партия.                                                                                                             "
                              "Весной 2023 началась выдача очень красивых партбилетов, удостоверяющих членство в партии.                                                                                                             "
                              "*Мы всегда рады новым членам! Вперёд, к счастливому будущему!*                                                                                                             "
                              "🦧🦍".format(
                             message.from_user))
        print(message.from_user.username, datetime.datetime.now())
    if message.text == '🪪 Хочу посмотреть на партбилет!':
        img3 = open('img3.png', 'rb')
        bot.send_photo(message.chat.id, img3)
        print(message.from_user.username, datetime.datetime.now())


bot.polling(none_stop=True, interval=0)
