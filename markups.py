from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Назад
btnMain = KeyboardButton('🖕🏻Назад')
btnMain2 = KeyboardButton('Назад🖕🏻')
#Обновление данных
btnUpdate = KeyboardButton('Обновить')
#Отмена операции
btnBack = KeyboardButton('Назад')

back = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)

#Глав меню
btnMenu = KeyboardButton('📄Задания')
btnOther = KeyboardButton('💁Инфо')
btnChat = KeyboardButton('💬Связь')
btnKorzina = KeyboardButton('🧺Корзина')
btnAdmin = KeyboardButton('👑Админ Панель')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnMenu, btnChat, btnKorzina,
                                                         btnOther)
mainMenu2 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(btnMenu, btnOther, btnChat, btnKorzina ,
                                                                       btnAdmin)

#Другое меню
update = ReplyKeyboardMarkup(resize_keyboard=True).add(btnUpdate, btnBack)


#Меню для чата:
btnOtv = KeyboardButton('Отправить')
btnDelete = KeyboardButton('Удалить')
btnOtmena = KeyboardButton('Отменить')
menuChat = ReplyKeyboardMarkup(resize_keyboard=True).row(btnOtv, btnDelete,  btnOtmena)


#Админ панель
btnVariant = KeyboardButton('Ред Вопросов')
btnOrders = KeyboardButton('Все Заказы')
btnOrdersAdmin = KeyboardButton('Мои Заказы')
btnRevision = KeyboardButton('Ревизия')
btnMailing = KeyboardButton('Рассылка')
btnLesson = KeyboardButton('Предметы')


AdminMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnVariant, btnOrders, btnOrdersAdmin,
                                                          btnRevision, btnMailing, btnLesson, btnMain)


#Добавление предмета
addLesson = KeyboardButton('Добавить Предмет')
LessonKey = ReplyKeyboardMarkup(resize_keyboard=True).add(addLesson, btnMain2)


#Aдмин панель блок и вариант кнопки
btnAddBlock = KeyboardButton('Добавить Блок')
btnDelBlock = KeyboardButton('Удалить Блок')
AdminAddBlockMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAddBlock, btnDelBlock,
                                                                  btnUpdate, btnMain2)
#Меню с добавление варианта и тд
btnAddQuestion = KeyboardButton('Добавить Задание')
btnDelQuestion = KeyboardButton('Удалить Задание')
btnAddPhoto = KeyboardButton('Добавить Фото')
AdminAddQuestionMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAddQuestion, btnDelQuestion,
                                                                  btnUpdate, btnBack)
AdminAddPhotoMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAddQuestion, btnDelQuestion,
                                                                  btnUpdate, btnAddPhoto, btnBack)

#Выбор курса
btnOne = KeyboardButton('1⃣')
btnTwo = KeyboardButton('2⃣')
btnThree = KeyboardButton('3⃣')
btnFour = KeyboardButton('4⃣')
SourseMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOne, btnTwo, btnThree, btnFour)

#Выбор курса 2
One = KeyboardButton('1')
Two = KeyboardButton('2')
Three = KeyboardButton('3')
Four = KeyboardButton('4')
Cifri = ReplyKeyboardMarkup(resize_keyboard=True).add(One, Two, Three, Four)





#Цены
btnPrice1 = KeyboardButton('50')
btnPrice2 = KeyboardButton('100')
btnPrice3 = KeyboardButton('150')
btnPrice4 = KeyboardButton('250')
btnPrice5 = KeyboardButton('350')
btnPrice6 = KeyboardButton('500')
btnPrice7 = KeyboardButton('750')
btnPrice8 = KeyboardButton('1000')

Prices = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPrice1, btnPrice2, btnPrice3, btnPrice4, btnPrice5, btnPrice6, btnPrice7, btnPrice8)



#Выбор y/n
btnYes = KeyboardButton('Да')
btnNo = KeyboardButton('Нет')
ynMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnYes, btnNo)





