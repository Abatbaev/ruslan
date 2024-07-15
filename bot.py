from aiogram import Bot,Dispatcher,types,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from keyboards import reg_menu

class Registration(StatesGroup):
    name = State()
    last_name = State()
    phone_num = State()
    email = State()
    adress = State()
    birth_day = State()



api ='7314561189:AAHf6XttLncRBTGp42G7wxzoi90lGuH-iI4'
PROXY_URL = "http://proxy.server:3128/"
bot = Bot(api,proxy=PROXY_URL)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)


@dp.message_handler(commands=['start'])
async def send_hi(xabar:types.Message):
    await xabar.answer(text='''Assalamuw alliykim botimizga xush
kelip siz! siz registraciyadan otiwiniz kerek''',reply_markup=reg_menu)


@dp.callback_query_handler()
async def send_reg(call:types.CallbackQuery):
    data = call.data
    if data=='reg':
        await bot.send_message(
            chat_id=call.from_user.id,
            text='OOO,taza qollaniwshi.bizge atinizdi jazip jiberin')
        await Registration.name.set()

@dp.message_handler(state=Registration.name)
async def send_name(message:types.Message,state:FSMContext):
    async with state.proxy() as magliwmat:
        magliwmat['name']=message.text
    await message.answer('Axa endi bizge familiyanizdi jazip qaldirin')
    await Registration.last_name.set()
@dp.message_handler(state=Registration.last_name)
async def send_surname(message:types.Message,state:FSMContext):
    async with state.proxy() as magliwmat:
        magliwmat['last_name']=message.text
    await message.answer('Axa endi bizge telefon numerinizdi jazip qaldirin')
    await Registration.phone_num.set()

@dp.message_handler(state=Registration.phone_num)
async def send_num(message:types.Message,state:FSMContext):
    async with state.proxy() as magliwmat:
        magliwmat['phone_num']=message.text
    await message.answer('Axa endi bizge email jazip qaldirin')
    await Registration.email.set()

@dp.message_handler(state=Registration.email)
async def send_name(message:types.Message,state:FSMContext):
    async with state.proxy() as magliwmat:
        magliwmat['email']=message.text
    await message.answer('Axa endi bizge jilinizdi jazip qaldirin')
    await Registration.birth_day.set()

@dp.message_handler(state=Registration.birth_day)
async def send_name(message:types.Message,state:FSMContext):
    async with state.proxy() as magliwmat:
        magliwmat['birth_day']=message.text
    await message.answer('Axa endi bizge adress jazip qaldirin')
    await Registration.adress.set()

@dp.message_handler(state=Registration.adress)
async def send_name(message:types.Message,state:FSMContext):
    async with state.proxy() as magliwmat:
        magliwmat['adress']=message.text
    await message.answer(f'''Axa siz egistration jumbaqladiniz

Ati:{magliwmat['name']}
Familiyasi:{magliwmat['last_name']}
Telefonnomeri:{magliwmat['phone_num']}
Jili:{magliwmat['birth_day']}
Adress:{magliwmat['adress']}
Email:{magliwmat['email']}
''')
    await state.finish()
if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)