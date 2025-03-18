from aiogram import Router, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router_boards = Router(name='jon')

#основное меню
all_page_one = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Проблемы с входом ", callback_data="locer")],
    [InlineKeyboardButton(text="Проблема 'сюрпризы после гостей'", callback_data="guest")],
    [InlineKeyboardButton(text="Проблема с постельным", callback_data="bedding")],
    [InlineKeyboardButton(text="Проблемы с раздаткой ", callback_data="consumables")],
])

all_page_two = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="что", callback_data="who")],
    [InlineKeyboardButton(text="что", callback_data="who")],
    [InlineKeyboardButton(text="что", callback_data="who"),InlineKeyboardButton(text="что", callback_data="who")],
    [InlineKeyboardButton(text="прошлая ", callback_data="last_page_all"),
     InlineKeyboardButton(text="следующая", callback_data="next_page_all")],
])


#Локер
locer_all = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="В локере нет ключей", callback_data="problem locer_1")],
    [InlineKeyboardButton(text="Локер не открывается", callback_data="problem locer_2")],
    [InlineKeyboardButton(text="Локер сломан", callback_data="problem locer_3")],
    [InlineKeyboardButton(text="Локера нет на его месте", callback_data="problem locer_4")],
    [InlineKeyboardButton(text="В локере есть ключи, но ещё нет 10:00", callback_data="problem locer_5")],
    [InlineKeyboardButton(text="Дверь в квартиру не открывается", callback_data="problem locer_6")],
    [InlineKeyboardButton(text="Гости ещё в квартире (SOS гости не выехали вовремя, extra time за ожидание)", callback_data="problem locer_7")],
    [InlineKeyboardButton(text="Проблемы нет в списке", callback_data="add_problem_locer")]
])


#последняя страница локера
last_page_locer = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="вернуться", callback_data="return_locer")],[InlineKeyboardButton(text="проблема решена", callback_data="locer_decided")]
])

#гости
guest_trouble_all =InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Квартира в ужасном состоянии", callback_data="problem guest_trouble_1")],
    [InlineKeyboardButton(text="Поломки и неисправности", callback_data="problem guest_trouble_2")],
    [InlineKeyboardButton(text="Забытые вещи ", callback_data="problem guest_trouble_3")],
    [InlineKeyboardButton(text="Оставленные деньги ", callback_data="problem guest_trouble_4")],
    [InlineKeyboardButton(text="Проблемы нет в списке", callback_data="problem add_problem_guest")],
])


#последняя страница гости
last_page_guest = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="вернуться", callback_data="return_guest")],[InlineKeyboardButton(text="проблема решена", callback_data="guest_decided")]
])
#постельное
bedding = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Курьера нет, нечем работать", callback_data="problem bedding_1")],
    [InlineKeyboardButton(text="Брак постельного", callback_data="problem bedding_2")],
    [InlineKeyboardButton(text="Уборка закончена, курьера нет", callback_data="problem bedding_3")],
    [InlineKeyboardButton(text="Проблемы нет в списке", callback_data="add_problem_door")]
])

#последняя страница постельное
last_page_door = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="вернуться", callback_data="return_bedding")],[InlineKeyboardButton(text="проблема решена", callback_data="bedding_decided")]
])

#раздатка
consumables = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="SOS закончилась туал бумага", callback_data="problem consumables_1")],
    [InlineKeyboardButton(text="Нет основной раздатки", callback_data="problem consumables_2")],
    [InlineKeyboardButton(text="В контрольном списке нет пунктов из раздатки", callback_data="problem consumables_3")],
    [InlineKeyboardButton(text="Проблемы нет в списке", callback_data="add_problem_door")]
])


#авыавы
async def create_keyboards(buttons: list) -> InlineKeyboardMarkup:
    keyboards_list = []
    for button_info in buttons:
        keyboards_list.append([InlineKeyboardButton(text=button_info[0], callback_data=button_info[1])])

    return InlineKeyboardMarkup(inline_keyboard=keyboards_list)

#
async def create_keyboards_fi(buttons: list, recallback: str) -> InlineKeyboardMarkup:
    keyboards_list = []
    for button_info in buttons:
        keyboards_list.append([InlineKeyboardButton(text=button_info[0], callback_data=button_info[1])])
    keyboards_list.append(
        [InlineKeyboardButton(text="Вернуться", callback_data=recallback),InlineKeyboardButton(text="Проблема решена", callback_data="pronto")]
    )
    return InlineKeyboardMarkup(inline_keyboard=keyboards_list)

