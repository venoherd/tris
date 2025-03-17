from aiogram import Router, F
from aiogram.types import  CallbackQuery, Message
from data.keyboards import last_page_locer, last_page_door, all_page_one, locer_all, all_page_two, \
    last_page_guest, guest_trouble_all

router_boards_back = Router(name='Bobi')
#обработчики
@router_boards_back.message(F.text.lower() == "помощь")
async def rpoblem_main(message: Message):
    await message.reply(text="Если у вас возникла какая-то проблема, напишите в чат - \"проблема\", далее выберете с чем ваша проблема и найдите ее в списке! ")

#основное меню
@router_boards_back.message(F.text.lower() == "проблемы")
async def rpoblem_main(message: Message):
    await message.answer("Ниже представлен список всех проблем",reply_markup=all_page_one,)

@router_boards_back.message(F.text.lower() == "проблемы два")
async def rpoblem_main_two(message: Message):
    await message.answer("Ниже представлен список всех проблем",reply_markup=all_page_two,)

@router_boards_back.callback_query(F.data == "next_page_all")
async def nextpage(call:CallbackQuery):
    await call.message.edit_text(text="Ниже представлен список всех проблем",reply_markup=all_page_two)

@router_boards_back.callback_query(F.data == "last_page_all")
async def locer_1(call: CallbackQuery):
    await call.message.edit_text(text="Ниже представлен список всех проблем",reply_markup=all_page_one)

#локер
@router_boards_back.message(F.text.lower() == "проблема локер")
async def locer_f(message: Message):
    await message.reply("проблема не проблема",reply_markup=locer_all)

@router_boards_back.callback_query(F.data == "entry")
async def locer_f_1(call: CallbackQuery):
    await call.message.edit_text(text="Ниже представлен список всех проблем",reply_markup=locer_all)

#обработчик локера
#в локере нет ключей
@router_boards_back.callback_query(F.data == "ffff")
async def locer_1(call: CallbackQuery):
    await call.message.edit_text("тут", reply_markup=last_page_locer)
#Локер не открывается
@router_boards_back.callback_query(F.data == "locer_2")
async def locer_2(call: CallbackQuery):
    await call.message.edit_text("Локер не открывается \n \n1. Отправьте в чат фото локера издалека, чтобы супервайзер убедилась в том, что вы открываете наш локер. \n \n2. Одновременно сами убедитесь, что локер наш. \nСравните фото локера и расположение локера в программе в блоке \"как войти в квартиру\" \n \n3. Нужно поболтать локер, чтобы по звуку  понять есть ли ключи внутри \n \n4. Гости могут разместить ключи внутри локера неверно, из-за чего могут заблокировать локер, для этого нужно стукнуть локер \n \n5. Если не помогло, нужно перевернуть локер и открывать его в перевёрнутом положении", reply_markup=last_page_locer)
#Локер сломан
@router_boards_back.callback_query(F.data == "locer_3")
async def locer_3(call: CallbackQuery):
    await call.message.edit_text("тут", reply_markup=last_page_locer)
#Локера нет на его месте
@router_boards_back.callback_query(F.data == "locer_4")
async def locer_4(call: CallbackQuery):
    await call.message.edit_text("Локера нет на своем месте \n \n1. Отправляем в чат квартиры фото места, где раньше был локер. Фото должно быть сделано издалека. \n \n2. Проверяем информацию в программе о местоположении локера (локер иногда перемещают, нужно быть уверенными,что вы владеете е актуальной информацией) \n \n3. Если в квартиру можно войти без ключей (по ссылкам), то идём в квартиру, чтобы приступить к работе.", reply_markup=last_page_locer)
#В локере есть ключи, но ещё нет 10:00
@router_boards_back.callback_query(F.data == "locer_5")
async def locer_5(call: CallbackQuery):
    await call.message.edit_text("В локере есть ключи, но ещё нет 10:00 \n \nВажно знать, в эту квартиру можно войти только с ключом или по ссылке Vickey \n \nЕсли в квартире два локера- наш и гостевой, то проверяем оба локера! \n \nЕсли и гостевой и наши локер с ключами, значит гости уже освободили квартиру, но перед входом обязательно нужно позвонить в дверь", reply_markup=last_page_locer)
#Дверь в квартиру не открывается
@router_boards_back.callback_query(F.data == "locer_6")
async def locer_6(call: CallbackQuery):
    await call.message.edit_text("тут", reply_markup=last_page_locer)
#Гости ещё в квартире (SOS гости не выехали вовремя, extra time за ожидание)
@router_boards_back.callback_query(F.data == "locer_7")
async def locer_7(call: CallbackQuery):
    await call.message.edit_text("тут", reply_markup=last_page_locer)


@router_boards_back.callback_query(F.data == "return_locer")
async def locer_r(call: CallbackQuery):
    await call.message.edit_text("проблема не проблема",reply_markup=locer_all)

@router_boards_back.callback_query(F.data == "add_problem")
async def locer_add(call: CallbackQuery):
    await call.message.edit_text("Опишите проблему!")

@router_boards_back.callback_query(F.data == "locer_decided")
async def locer_dec(call: CallbackQuery):
    await call.message.edit_text("Отлично!")

#дверь


@router_boards_back.callback_query(F.data == "guest_trouble")
async def locer_dec(call: CallbackQuery):
    await call.message.edit_text("проблема не проблема",reply_markup=guest_trouble_all)


#обработчик двери
@router_boards_back.callback_query(F.data == "door_1")
async def door_1(call: CallbackQuery):
    await call.message.edit_text("тут", reply_markup=last_page_door)

@router_boards_back.callback_query(F.data == "door_2")
async def door_2(call: CallbackQuery):
    await call.message.edit_text("тут", reply_markup=last_page_door)

@router_boards_back.callback_query(F.data == "door_3")
async def door_3(call: CallbackQuery):
    await call.message.edit_text("тут", reply_markup=last_page_door)


@router_boards_back.callback_query(F.data == "add_problem")
async def door_add(call: CallbackQuery):
    await call.message.edit_text("Опишите проблему!")

@router_boards_back.callback_query(F.data == "door_decided")
async def door_dec(call: CallbackQuery):
    await call.message.edit_text("Отлично!")

#гости
@router_boards_back.message(F.text.lower() == "проблема гости")
async def door_f(message: Message):
    await message.reply("проблема не проблема",reply_markup="guest_trouble")

#обработчик гости
@router_boards_back.callback_query(F.data == "guests_1")
async def door_1(call: CallbackQuery):
    await call.message.edit_text("тут", reply_markup=last_page_guest)

@router_boards_back.callback_query(F.data == "guests_2")
async def door_2(call: CallbackQuery):
    await call.message.edit_text("тут", reply_markup=last_page_guest)

@router_boards_back.callback_query(F.data == "guests_3")
async def door_3(call: CallbackQuery):
    await call.message.edit_text("тут", reply_markup=last_page_guest)

@router_boards_back.callback_query(F.data == "return_guests")
async def door_r(call: CallbackQuery):
    await call.message.edit_text("проблема не проблема",reply_markup=guest_trouble_all)

@router_boards_back.callback_query(F.data == "add_problem")
async def door_add(call: CallbackQuery):
    await call.message.edit_text("Опишите проблему!")

@router_boards_back.callback_query(F.data == "guests_decided")
async def door_dec(call: CallbackQuery):
    await call.message.edit_text("Отлично!")



#как должна выглядеть эта функция
@router_boards_back.callback_query(F.data == "locer_1")
async def locer_1(call: CallbackQuery):
    await call.message.edit_text(text="", reply_markup=last_page_locer)