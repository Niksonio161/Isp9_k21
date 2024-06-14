from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

balance_ikb = InlineKeyboardMarkup(row_width=1,
                                   inline_keyboard=[
                                       [InlineKeyboardButton(text='Пополнить баланс',
                                                             callback_data='add_balance')]
                                   ])

cancel_balance_ikb = InlineKeyboardMarkup(row_width=1,
                                          inline_keyboard=[
                                              [InlineKeyboardButton(text='Отменить❌',
                                                                    callback_data='balance_cancel')]
                                          ])

plans_ikb = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [InlineKeyboardButton(text='1 час(110р.)',
                                                           callback_data='hour_1'),
                                      InlineKeyboardButton(text='3 часа(300р.)',
                                                           callback_data='hour_3')
                                      ],
                                     [InlineKeyboardButton(text='5 часов(500р.)',
                                                           callback_data='hour_5'),
                                      InlineKeyboardButton(text='10 часов(900р.)',
                                                           callback_data='hour_10')]
                                 ])
