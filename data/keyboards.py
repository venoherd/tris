from aiogram import Router, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router_boards = Router(name='jon')

#основное меню
all_page_one = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Проблемы с входом ", callback_data="entry")],
    [InlineKeyboardButton(text="Проблема 'сюрпризы после гостей'", callback_data="guest_trouble")],
    [InlineKeyboardButton(text="Проблема с постельным", callback_data="bedding")],
    [InlineKeyboardButton(text="Проблемы с раздаткой ", callback_data="consumables")],
    [InlineKeyboardButton(text="Следующая страница ", callback_data="next_page_all")]
])

all_page_two = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="что", callback_data="who")],
    [InlineKeyboardButton(text="что", callback_data="who")],
    [InlineKeyboardButton(text="что", callback_data="who")],
    [InlineKeyboardButton(text="что", callback_data="who")],
    [InlineKeyboardButton(text="Предыдущая страница", callback_data="last_page_all")]
])



#Локер
locer_all = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="В локере нет ключей", callback_data="locer_1")],
    [InlineKeyboardButton(text="Локер не открывается", callback_data="locer_2")],
    [InlineKeyboardButton(text="Локер сломан", callback_data="locer_3")],
    [InlineKeyboardButton(text="Локера нет на его месте", callback_data="locer_4")],
    [InlineKeyboardButton(text="В локере есть ключи, но ещё нет 10:00", callback_data="locer_5")],
    [InlineKeyboardButton(text="Дверь в квартиру не открывается", callback_data="locer_6")],
    [InlineKeyboardButton(text="Гости ещё в квартире (SOS гости не выехали вовремя, extra time за ожидание)", callback_data="locer_7")],
    [InlineKeyboardButton(text="Проблемы нет в списке", callback_data="add_problem_locer")]
])


#последняя страница локера
last_page_locer = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="вернуться", callback_data="return_locer")],[InlineKeyboardButton(text="проблема решена", callback_data="locer_decided")]
])

#добавление проблемы локера
#сделаю но позже

#гости
guest_trouble_all =InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Квартира в ужасном состоянии", callback_data="guest_trouble_1")],
    [InlineKeyboardButton(text="Поломки и неисправности", callback_data="guest_trouble_2")],
    [InlineKeyboardButton(text="Забытые вещи ", callback_data="guest_trouble_3")],
    [InlineKeyboardButton(text="Оставленные деньги ", callback_data="guest_trouble_4")],
    [InlineKeyboardButton(text="Проблемы нет в списке", callback_data="add_problem_guest")],
])


#последняя страница гости
last_page_guest = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="вернуться", callback_data="return_guest")],[InlineKeyboardButton(text="проблема решена", callback_data="guest_decided")]
])
#Двери
door = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Не могу открыть дверь в здание", callback_data="door_1")],
    [InlineKeyboardButton(text="Не могу открыть дверь в квартиру", callback_data="door_2")],
    [InlineKeyboardButton(text="Проблема с ключами", callback_data="door_3")],
    [InlineKeyboardButton(text="Проблемы нет в списке", callback_data="add_problem_door")]
])

#последняя страница двери
last_page_door = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="вернуться", callback_data="return_door")],[InlineKeyboardButton(text="проблема решена", callback_data="door_decided")]
])

#постельное


#Вещи
#Поломка

