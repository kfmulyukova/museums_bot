from aiogram import Bot, Dispatcher, executor, types
import sqlite3

from keyboards import markups as kb
from config import config
from data import text_data as te

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

gg = []

rate1 = []
rate2 = []

admin_id = []

file_id = 0

mailing = 0

state = 0

user_id = []

score = 0
idd = 0

base = sqlite3.connect('table.db')
cur = base.cursor()

@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message):
    global user_id
    user_name = msg.from_user.username
    us_id = msg.from_user.id
    id = msg.chat.id
    await bot.send_message(id, te.START1 + str(user_name) + te.START2, reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message_id)
    if us_id not in user_id:
        user_id.append(us_id)
        print(user_id)

@dp.message_handler(commands=['setup'])
async def start_cmd(message: types.Message):
    global state
    await bot.send_message(message.from_user.id, te.ENTER_KEY, reply_markup=kb.cancel)
    state = 1
    await bot.delete_message(message.from_user.id, message.message_id)

@dp.message_handler(commands=['mailing'])
async def start_cmd(msg: types.Message):
    global state

    await bot.send_message(msg.from_user.id, te.MAILING_INFO)
    state = 2

@dp.callback_query_handler(text='info')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu_osn)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='history_alma')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.HISTORY_ALMA_TEXT,reply_markup=kb.alma)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
#Конкурс
@dp.callback_query_handler(text='info_konkurs')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.INFO_KONKURS,reply_markup=kb.alma_back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='quiz')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.HISTORY_ALMA_TEXT,reply_markup=kb.alma_quiz)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)



@dp.callback_query_handler(text='start_ask')
async def menu(msg: types.Message):
    global score
    global idd
    base.execute('CREATE TABLE IF NOT EXISTS {}(id PRIMARY KEY,username,score)'.format('data'))
    cur.execute('INSERT INTO data VALUES(?,?,?)', (idd, msg.from_user.username, score))
    base.commit()
    idd += 1
    await bot.send_message(msg.from_user.id,te.QUEST1,reply_markup=kb.quiz1)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score+=0


@dp.callback_query_handler(text='otv11')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST2, reply_markup=kb.quiz2)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score -= 1


@dp.callback_query_handler(text='otv12')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST2, reply_markup=kb.quiz2)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score += 1


@dp.callback_query_handler(text='otv13')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST2, reply_markup=kb.quiz2)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score -= 1


@dp.callback_query_handler(text='otv21')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST3, reply_markup=kb.quiz3)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score -= 1


@dp.callback_query_handler(text='otv22')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST3, reply_markup=kb.quiz3)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score -= 1


@dp.callback_query_handler(text='otv23')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST3, reply_markup=kb.quiz3)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score += 1


@dp.callback_query_handler(text='otv31')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST4, reply_markup=kb.quiz4)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score += 1


@dp.callback_query_handler(text='otv32')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST4, reply_markup=kb.quiz4)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score -= 1


@dp.callback_query_handler(text='otv33')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST4, reply_markup=kb.quiz4)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score -= 1


@dp.callback_query_handler(text='otv41')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST5, reply_markup=kb.quiz5)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score += 1


@dp.callback_query_handler(text='otv42')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST5, reply_markup=kb.quiz5)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score -= 1


@dp.callback_query_handler(text='otv43')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST5, reply_markup=kb.quiz5)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score -= 1


@dp.callback_query_handler(text='otv51')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST6, reply_markup=kb.quiz6)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score -= 1


@dp.callback_query_handler(text='otv52')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST6, reply_markup=kb.quiz6)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score += 1


@dp.callback_query_handler(text='otv53')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST6, reply_markup=kb.quiz6)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score -= 1


@dp.callback_query_handler(text='otv61')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST7, reply_markup=kb.quiz7)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score += 1


@dp.callback_query_handler(text='otv62')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST7, reply_markup=kb.quiz7)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score -= 1


@dp.callback_query_handler(text='otv63')
async def menu(msg: types.Message):
    global score
    await bot.send_message(msg.from_user.id, te.QUEST7, reply_markup=kb.quiz7)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    score -= 1


@dp.callback_query_handler(text='otv71')
async def menu(msg: types.Message):
    global score
    global idd
    global rate1
    global rate2

    score -= 1

    await bot.send_message(msg.from_user.id, te.SCORE+str(score)+te.SCORE_OST, reply_markup=kb.alma)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

    rate2.append(score)
    rate1.append(msg.from_user.username)

    cur.execute('UPDATE data SET score == ? WHERE id == ?', (score,idd-1))
    base.commit()
    score=0


@dp.callback_query_handler(text='otv72')
async def menu(msg: types.Message):
    global score
    global idd
    global rate1
    global rate2

    score += 1

    await bot.send_message(msg.from_user.id, te.SCORE+str(score)+te.SCORE_OST, reply_markup=kb.alma)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

    rate2.append(score)
    rate1.append(msg.from_user.username)

    cur.execute('UPDATE data SET score == ? WHERE id == ?', (score,idd-1))
    base.commit()
    score=0

@dp.callback_query_handler(text='otv73')
async def menu(msg: types.Message):
    global score
    global idd
    global rate1
    global rate2

    score -= 1


    await bot.send_message(msg.from_user.id, te.SCORE+str(score)+te.SCORE_OST, reply_markup=kb.alma)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

    rate2.append(score)
    rate1.append(msg.from_user.username)
    print(rate2)
    print(rate1)

    cur.execute('UPDATE data SET score == ? WHERE id == ?', (score,idd-1))
    base.commit()
    score = 0

@dp.callback_query_handler(text='mailing')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.MAILING_TEXT,reply_markup=kb.mailing)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='rate')
async def menu(msg: types.Message):
    global rate1
    global rate2
    id = msg.from_user.id
    vivod = 0
    vivod2 = []

    while len(rate2) > 5:
        rate1.pop(0)
        rate2.pop(0)
    while len(rate2) < 5:
        rate1.append('zero')
        rate2.append(-7)

    def bubble_sort(nums,nums2):
        # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    # Меняем элементы
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    nums2[i], nums2[i + 1] = nums2[i + 1], nums2[i]
                    # Устанавливаем swapped в True для следующей итерации
                    swapped = True
    bubble_sort(rate2,rate1)
    await bot.send_message(msg.from_user.id,'Рейтинг (топ 5):\n\n'+str(rate1[4])+' = '+str(rate2[4])+'\n'+str(rate1[3])+' = '+str(rate2[3])+'\n'+str(rate1[2])+' = '+str(rate2[2])+'\n'+str(rate1[1])+' = '+str(rate2[1])+'\n'+str(rate1[0])+' = '+str(rate2[0])+'\n',reply_markup=kb.alma_back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='off_on_mailing')
async def menu(msg: types.Message):
    global mailing
    id = msg.from_user.id
    mailing+=1
    if mailing % 2 ==1:
        await bot.send_message(id, te.ON_MAILING, reply_markup=kb.mailing)
        await bot.delete_message(msg.from_user.id, msg.message.message_id)
    elif mailing % 2 ==0:
        await bot.send_message(id, te.OFF_MAILING, reply_markup=kb.mailing)
        await bot.delete_message(msg.from_user.id, msg.message.message_id)
    if mailing == 10:
        mailing = 0

#Основное меню
@dp.callback_query_handler(text='history')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(chat_id=id,photo='https://tatfrontu.ru/gallery2/d/40738-3/dsc01383.jpg',caption=te.HISTORY_TEXT,reply_markup=kb.back )
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='my_museum')
async def menu(msg: types.Message):
    global gg
    gg.clear()
    id = msg.from_user.id
    await bot.send_message(id,te.MY_MUSEUM_TEXT,reply_markup=kb.my_museums)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='price')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(chat_id=id,photo='https://images.app.goo.gl/64JjEoEESNWB8fiP8',caption=te.PRICE_TEXT,reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='time_work')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(chat_id=id,photo='https://catherineasquithgallery.com/uploads/posts/2021-03/1614571359_102-p-chasi-na-belom-fone-111.png',caption=te.TIME_WORK_TEXT,reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='social')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_photo(chat_id=id,photo='https://lh6.googleusercontent.com/mGchpezu3D0dYIlg6Xtn1JLSEToK75Yj1i7qFihZzfmfbWMJkj1jwj9-OjLYB4VZiIo25rEWZ07WN6SdDL0zhXTUDmyixujsJ4pTPYjezaTTUQhmNRV0TbGJXeHdzQ8kXDcvSUyl',caption=te.SOCIAL_TEXT,reply_markup=kb.social)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

#Меню музеев
@dp.callback_query_handler(text='museum_1')
async def menu(msg: types.Message):
    global gg
    gg.append('Музей истории Казанского университета')
    id = msg.from_user.id
    await bot.send_message(id,te.MUSEUMS_1,reply_markup=kb.back_to_museum)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='museum_2')
async def menu(msg: types.Message):
    global gg
    gg.append('Геологический музей им. А.А. Штукенберга')
    id = msg.from_user.id
    await bot.send_message(id,te.MUSEUMS_2,reply_markup=kb.back_to_museum)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='museum_3')
async def menu(msg: types.Message):
    global gg
    gg.append('Музей Казанской химической школы')
    id = msg.from_user.id
    await bot.send_message(id,te.MUSEUMS_3,reply_markup=kb.back_to_museum)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='museum_4')
async def menu(msg: types.Message):
    global gg
    gg.append('Этнографический музей')
    id = msg.from_user.id
    await bot.send_message(id,te.MUSEUMS_4,reply_markup=kb.back_to_museum)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='museum_5')
async def menu(msg: types.Message):
    global gg
    gg.append('Музей-лаборатория Е.К. Завойского')
    id = msg.from_user.id
    await bot.send_message(id,te.MUSEUMS_5,reply_markup=kb.back_to_museum)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='museum_6')
async def menu(msg: types.Message):
    global gg
    gg.append('Музей Н.И. Лобачевского')
    id = msg.from_user.id
    await bot.send_message(id,te.MUSEUMS_6,reply_markup=kb.back_to_museum)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
#Даты
@dp.callback_query_handler(text='1')
async def menu(msg: types.Message):
    global gg
    gg.append('1')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_TIME,reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='2')
async def menu(msg: types.Message):
    global gg
    gg.append('2')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='3')
async def menu(msg: types.Message):
    global gg
    gg.append('3')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='4')
async def menu(msg: types.Message):
    global gg
    gg.append('4')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='5')
async def menu(msg: types.Message):
    global gg
    gg.append('5')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='6')
async def menu(msg: types.Message):
    global gg
    gg.append('6')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='7')
async def menu(msg: types.Message):
    global gg
    gg.append('7')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='8')
async def menu(msg: types.Message):
    global gg
    gg.append('8')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='9')
async def menu(msg: types.Message):
    global gg
    gg.append('9')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='10')
async def menu(msg: types.Message):
    global gg
    gg.append('10')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='11')
async def menu(msg: types.Message):
    global gg
    gg.append('11')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='12')
async def menu(msg: types.Message):
    global gg
    gg.append('12')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='13')
async def menu(msg: types.Message):
    global gg
    gg.append('13')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='14')
async def menu(msg: types.Message):
    global gg
    gg.append('14')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='15')
async def menu(msg: types.Message):
    global gg
    gg.append('15')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='16')
async def menu(msg: types.Message):
    global gg
    gg.append('16')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='17')
async def menu(msg: types.Message):
    global gg
    gg.append('17')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='18')
async def menu(msg: types.Message):
    global gg
    gg.append('18')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='19')
async def menu(msg: types.Message):
    global gg
    gg.append('19')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='20')
async def menu(msg: types.Message):
    global gg
    gg.append('20')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='21')
async def menu(msg: types.Message):
    global gg
    gg.append('21')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='22')
async def menu(msg: types.Message):
    global gg
    gg.append('22')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='23')
async def menu(msg: types.Message):
    global gg
    gg.append('23')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='24')
async def menu(msg: types.Message):
    global gg
    gg.append('24')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='25')
async def menu(msg: types.Message):
    global gg
    gg.append('25')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='26')
async def menu(msg: types.Message):
    global gg
    gg.append('26')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='27')
async def menu(msg: types.Message):
    global gg
    gg.append('27')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='28')
async def menu(msg: types.Message):
    global gg
    gg.append('28')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
#Время
@dp.callback_query_handler(text='10:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(id,
                           te.FINAL_EXCURS + str(gg[2]) + ' ' + str(gg[1]) + '\n в ' + str(gg[0]) + '\n на время : '+'10:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='11:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(id,
                           te.FINAL_EXCURS + str(gg[2]) + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '11:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='12:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(id,
                           te.FINAL_EXCURS + str(gg[2]) + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '12:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='13:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(id,
                           te.FINAL_EXCURS + str(gg[2]) + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '13:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='14:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(id,
                           te.FINAL_EXCURS + str(gg[2]) + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '14:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='15:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(id,
                           te.FINAL_EXCURS + str(gg[2]) + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '15:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='16:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(id,
                           te.FINAL_EXCURS + str(gg[2]) + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '16:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='17:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(id,
                           te.FINAL_EXCURS + str(gg[2]) + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '17:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    gg.clear()


#Вывод данных

#месяца
@dp.callback_query_handler(text='jan')
async def menu(msg: types.Message):
    global gg
    gg.append('Января')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='feb')
async def menu(msg: types.Message):
    global gg
    gg.append('Февраля')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='mar')
async def menu(msg: types.Message):
    global gg
    gg.append('Марта')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='apr')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='mai')
async def menu(msg: types.Message):
    global gg
    gg.append('Мая')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='iun')
async def menu(msg: types.Message):
    global gg
    gg.append('Июня')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='iul')
async def menu(msg: types.Message):
    global gg
    gg.append('Июля')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='avg')
async def menu(msg: types.Message):
    global gg
    gg.append('Августа')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='sent')
async def menu(msg: types.Message):
    global gg
    gg.append('Сентября')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='okt')
async def menu(msg: types.Message):
    global gg
    gg.append('Октября')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='noyab')
async def menu(msg: types.Message):
    global gg
    gg.append('Ноября')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='dec')
async def menu(msg: types.Message):
    global gg
    gg.append('Декабря')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.message_handler(content_types=["photo"])
async def get_photo(message):
    global file_id
    global user_id
    global admin_id

    if message.from_user.id in admin_id:
        file_id = message.photo[-1].file_id
        caption = message.caption
        print(file_id) # этот идентификатор нужно где-то сохранить
        await bot.delete_message(message.from_user.id, message.message_id)
        for i in user_id:
            try:
                await bot.send_photo(chat_id=i, photo=file_id, caption=caption)
                state = 0
            except Exception as e:
                print('сырный тут')
    else:
        await bot.delete_message(message.from_user.id, message.message_id)
#Записать на экскурсию
@dp.callback_query_handler(text='excursion_mount')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_MOUNT,reply_markup=kb.mount)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='excursion_date')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

#Викторина



#Кнопки назад
@dp.callback_query_handler(text='back_to_museum')
async def menu(msg: types.Message):
    global gg
    gg.clear()
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.my_museums)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='back_to_menu')
async def menu(msg: types.Message):
    global gg
    gg.clear()
    id = msg.from_user.id
    await bot.send_message(id,te.OSN_TEXT,reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='back_to_osn')
async def menu(msg: types.Message):
    global gg
    gg.clear()
    id = msg.from_user.id
    await bot.send_message(id,te.BACK_TEXT,reply_markup=kb.menu_osn)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='back_to_alma')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.HISTORY_ALMA_TEXT,reply_markup=kb.alma)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='cancel')
async def cancel(msg: types.Message):
    global state

    state = 0
    await bot.send_message(msg.from_user.id,te.EXIT)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all_other_messages(message: types.Message):
    global state
    global admin_id
    # await bot.send_message(message.from_user.id,'Не понял вас')
    g = message.from_user.id
    d = message.message_id

    if state == 1:
        if message.text == te.ADMIN_KEY:
            await bot.send_message(g, te.ACCES)
            await bot.delete_message(g, d)
            await bot.delete_message(g, d - 1)
            if message.from_user.id not in admin_id:
                admin_id.append(g)
                state = 0
        else:
            await bot.send_message(g, te.NOTACCES, reply_markup=kb.cancel)
            await bot.delete_message(g, d)
            await bot.delete_message(g, d - 1)
    elif state == 2:
        for i in user_id:
            try:
                await bot.send_message(i,message.text)
                state = 0
            except Exception as e:
                print('ошибка')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
