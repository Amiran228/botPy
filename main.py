import logging
import time

from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '5922594528:AAEgkkNcSNnMyA_o0JnbqwO6oBl4m4Bax5Y'  # никуда не скидывать

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# button_start = KeyboardButton()

start_button = [
    [
        types.KeyboardButton(text='/start'),
        types.KeyboardButton(text='/menu'),
        types.KeyboardButton(text='/techsupport'),
        types.KeyboardButton(text='/howtouse')
    ],
]


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard_start = types.ReplyKeyboardMarkup(keyboard=start_button)
    user_id = message.from_user.id
    # user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}", reply_markup=keyboard_start)


menuKB = InlineKeyboardMarkup(row_width=1)
menuButton = InlineKeyboardButton(text='Человек и общество', callback_data="menu_human_and_society")
menuButton2 = InlineKeyboardButton(text='Социальные отношения', callback_data="menu_social_relations")
menuButton3 = InlineKeyboardButton(text='чет 1', callback_data="menu_3")
menuButton4 = InlineKeyboardButton(text='чет 2 ', callback_data="menu_4")
menuButton5 = InlineKeyboardButton(text='чет 3', callback_data="menu_5")
menuKB.add(menuButton, menuButton2, menuButton3, menuButton4, menuButton5)


@dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
    await message.answer('тут меню', reply_markup=menuKB)
    # await message.reply()
    # await callback.answer();


text_human_and_society = 'ЧЕЛОВЕК И ОБЩЕСТВО\n \n1. Деятельность \n2. Познание \n3. Истина \n4. Человек \n5. Сознание' \
                         '\n6. Чувственное познание \n7. Рациональное познание \n8. Социальное познание \n9. Научное познание (наука) ' \
                         '\n10. Мировоззрение \n11. Мышление \n12. Искусство \n13. Образование \n14. Религия \n15. Мировые религии \n16. ' \
                         'Мораль \n17. Способности' \
                         '\n18. Социальное познание \n19. Общение как вид деятельности \n20. Игра как вид деятельности \n21. Потребность ' \
                         '\n22. Социальные ценности \n23. Свобода \n24. Общество как система \n25. Общество как часть материального мира ' \
                         '\n26. Ответственность \n27.Социальный институт \n28. Культура  \n29. Элитарная культура \n30. Массовая культура ' \
                         '\n31. Народная культура \n32. Реформа \n33. Революция \n34. Общественный прогресс \n35. Традиционное общество ' \
                         '\n36. Индустриальное общество \n37. Постиндустриальное общество \n38. Глобализация \n39. Глобальные проблемы человечества'
text_social_relations = 'Социальные отношения \n \n1. Семья как малая группа \n2. Социальные ценности \3. Социальные нормы \n4. Отклоняющееся поведение' \
                        '\n5. Социальный контроль \n6. Социальный конфликт \n7. Социализация \n8. Социальный статус \n9. Социальная роль' \
                        '\n10. Социальная стратификация \n11. Социальная мобильность \n12. Личность \n13. Нация \n14. Социальная группа \n15. Молодежь ' \
                        '\n16. Этнос (этническая общность) \n17. Этносоциальный конфликт \n18. Межнациональные отношения \n19. Антисоциальное поведение' \
                        '\n20. Малая группа \n21. Молодежная субкультура '


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('menu_'))  # обработчик инлайн кнопок меню
async def process_callback_menubutton(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    code = callback_query.data
    logging.info({code})

    if code == 'menu_human_and_society':
        await bot.send_message(chat_id=user_id,
                               text=text_human_and_society)

        @dp.message_handler()
        async def human_and_society(message: types.Message):
            user_id2 = message.from_user.id
            message_name = message.text
            user_full_name = message.from_user.full_name
            logging.info(f'{user_id2} {user_full_name} {time.asctime()} {message_name}')
            if message_name == '1':
                await message.answer(text='Деятельность'
                                          '\n1. направленность на преобразование окружающего мира и самого человека;'
                                          '\n2. осознанность и целенаправленность;'
                                          '\n3. общественный характер;'
                                          '\n4. продуктивный характер др.; ')
            elif message_name == '2':
                await message.answer(text='Познание'
                                          '\n1. процесс получения и обновления знания '
                                          '\n2. вид и результат деятельности субъекта познания человека;'
                                          '\n3.активное отражение действительности в сознании человека')
            elif message_name == '3':
                await message.answer(text='Истина'
                                          '\n1. соответствует свойствам объекта познания'
                                          '\n2. конкретна '
                                          '\n3. объективна')
            elif message_name == '4':
                await message.answer(text='Человек'
                                          '\n1. обладает членораздельной речью и мышлением'
                                          '\n2. может создавать сложные орудия труда '
                                          '\n3. наличие духовных и социальных потребностей ')
            elif message_name == '5':
                await message.answer(text='Сознание'
                                          '\n1. свойственно только людям'
                                          '\n2. функция мозга, связанная с речью'
                                          '\n3. заключается в обобщенном отражении действительности ')
            elif message_name == '6':
                await message.answer(text='Чувственное познание'
                                          '\n1. непосредственный контакт органов чувств с познаваемым объектом'
                                          '\n2. мнаглядность и предметность'
                                          '\n3. воспроизведение внешних сторон и свойств объекта')
            elif message_name == '7':
                await message.answer(text='Рациональное познание'
                                          '\n1. логические операции'
                                          '\n2. опора на результаты чувственного познания'
                                          '\n3. абстрактность и обобщенность'
                                          '\n4. выявление существенных свойств, закономерных связей и отношений')
            elif message_name == '8':
                await message.answer(text='Социальное познание'
                                          '\n1. субъект и объект познания совпадают,'
                                          '\n2. получаемое социальное знание всегда связано с интересами субъектов познания'
                                          '\n3. сложность объекта познания (общество находится в постоянном развитии)'
                                          '\n4. ограниченная возможность применения такого метода как эксперимент')
            elif message_name == '9':
                await message.answer(text='Научное познание'
                                          '\n1. объективность'
                                          '\n2. проверяемость, воспроизводимость знаний'
                                          '\n3. системность'
                                          '\n4. доказательность'
                                          '\n5. наличие специального языка науки, высокая степень обобщения и абстрактности научных категорий'
                                          '\n6. использование специальных способов и инструментов познавательной деятельности')
            elif message_name == '10':
                await message.answer(text='Мировоззрение'
                                          '\n1. всегда исторично (тесно связано с переживаемыми обществом стадиями развития, совокупностью тех проблем, которыми живет общество)'
                                          '\n2. сказывается на всем облике человека, на всей совокупности особенностей поведения и действий, привычек и наклонностей'
                                          '\n3. определяет общую направленность личности - совокупность устойчивых мотивов, ориентирующих ее деятельность')
            elif message_name == '11':
                await message.answer(text='Мышление'
                                          '\n1. способность к познанию существенных свойств и связей объектов'
                                          '\n2. выходит за рамки чувственной информации и практического опыта'
                                          '\n3. опосредованный характер (познающий человек с помощью мышления проникает в скрытые свойства, связи, отношения предметов, недоступные для органов чувств)'
                                          '\n4. обобщенность (результат мышления - сжатая модель действительности, переработанная информация)'
                                          '\n5. личностный характер мышления (это проявляется в том, какие задачи привлекают внимание того или иного человека, как он решает каждую из них, какие испытывает чувства при их решении).')
            elif message_name == '12':
                await message.answer(text='Искусство'
                                          '\n1. образность и наглядность'
                                          '\n2. отражение действительности при помощи художественных образов'
                                          '\n3. чувственное восприятие окружающего мира'
                                          '\n4.	ярко выраженный субъективный характер')
            elif message_name == '13':
                await message.answer(text='Образование'
                                          '\n1.	охватывает процесс овладения знаниями'
                                          '\n2.	связано с воспитанием и развитием интеллектуальных и творческих способностей, мировоззрения, личностных качеств человек'
                                          '\n3.	может быть организовано специальными учреждениями, а также на самостоятельной основе '
                                          '\nЧерты образования в информационном обществе:'
                                          '\n1.	демократичность'
                                          '\n2.	гибкость'
                                          '\n3.	непрерывность')
            elif message_name == '14':
                await message.answer(text='Религия'
                                          '\n1.	наличие организаций, форм объединения верующих'
                                          '\n2.	обусловленность верой в сверхъестественное'
                                          '\n3.	включает в себя свод моральных норм и правил поведения, обряды и культовые действия')
            elif message_name == '15':
                await message.answer(text='Мировые религии'
                                          '\n1.	носят наднациональный характер '
                                          '\n2.	имеют большое число последователей '
                                          '\n3.	проповедуют формальное равенство людей ')
            elif message_name == '16':
                await message.answer(text='Мораль'
                                          '\n1.	отсутствие четко очерченных границ,'
                                          '\n2.	мораль не имеет специальных организаций, которые создавали бы моральные нормы и контролировали их исполнение,'
                                          '\n3.	моральные нормы возникают стихийно, как отражение потребностей общества,'
                                          '\n4.	мораль требует от человека определенного поведения, '
                                          '\n5.	мораль не формализована, она позволяет оценить поведение людей в любой жизненной ситуации,'
                                          '\n6.	основой морали является внутренняя мотивация человека и механизмы самоконтроля')
            elif message_name == '17':
                await message.answer(text='Способности'
                                          '\n1.	обеспечивают успешность выполнения определенного рода деятельности'
                                          '\n2.	 развиваются постепенно в процессе обучения и освоения соответствующей деятельности '
                                          '\n3.	их развитие зависит от активности и целеустремленности самого человека')
            elif message_name == '18':
                await message.answer(text='Социальное познание'
                                          '\n1.	субъект и объект познания совпадают '
                                          '\n2.	субъективный характер '
                                          '\n3.	ограничение на проведение эксперимента ')
            elif message_name == '19':
                await message.answer(text='Общение как вид деятельности '
                                          '\n1.	предполагает обмен информацией, мыслями '
                                          '\n2.	предполагает наличие двух сторон, то есть партнёра'
                                          '\n3.	оно может выступать как самостоятельный вид деятельности, так и выступать элементом в других видах деятельности ')
            elif message_name == '20':
                await message.answer(text='Игра как вид деятельности '
                                          '\n1.	ориентация не на результат, а на процесс '
                                          '\n2.	создание условной воображаемой обстановки '
                                          '\n3.	осуществляются по определенным правилам '
                                          '\n4.	помогает примерять играющему новые социальные роли')
            elif message_name == '21':
                await message.answer(text='Потребность '
                                          '\n1.	нужда человека в том, что необходимо для его жизни и развития'
                                          '\n2.	являются мотивами деятельности, лежат в основе активности человека'
                                          '\n3.	переживается и осознается человеком '
                                          '\n4.	осознание потребности всегда сопровождается эмоциями человека')
            elif message_name == '22':
                await message.answer(text='Социальные ценности'
                                          '\n1.	их разделяют большинство людей '
                                          '\n2.	связаны с общественными идеалами, нормами и стандартами поведения'
                                          '\n3.	содержание и значение социальных ценностей зависит от культуры конкретного общества '
                                          '\n4.	выражаются в представлениях о добром, злом, справедливом, плохом, хорошем*')
            elif message_name == '23':
                await message.answer(text='Свобода '
                                          '\n1.	возможность человека осуществлять осознанный выбор'
                                          '\n2.	свобода не абсолютна, она может быть ограничена законом'
                                          '\n3.	выбор всегда связан с нравственным, интеллектуальным и волевым напряжением человека.')
            elif message_name == '24':
                await message.answer(text='Общество как система '
                                          '\n1.	динамичность'
                                          '\n2.	сложный характер '
                                          '\n3.	саморазвивающаяся '
                                          '\n4.	самодостаточность ')
            elif message_name == '25':
                await message.answer(text='Общество как часть материального мира '
                                          '\n1.	часть материального мира '
                                          '\n2.	связь с природой '
                                          '\n3.	включает в себя формы объединения и способы взаимодействия людей ')
            elif message_name == '26':
                await message.answer(text='Ответственность'
                                          '\n1.	способность осознавать последствия своих поступков '
                                          '\n2.	связана со свободой, без свободы не может быть ответственности'
                                          '\n3.	несёт определенные ограничения (лишения) действий')
            elif message_name == '27':
                await message.answer(text='Социальный институт'
                                          '\n1.	форма организации совместной деятельности людей '
                                          '\n2.	наличие социальных норм и правил, регулирующих поведение людей '
                                          '\n3.	наличие установок, образцов поведения  '
                                          '\n4.	удовлетворяют определенные общественные потребности ')
            elif message_name == '28':
                await message.answer(text='Культура'
                                          '\n1.	совокупность искусственных объектов, созданных человеком в процессе освоения и преобразования природы;'
                                          '\n2.	культура любой исторической эпохи неоднородна'
                                          '\n3.	характеризуется творческим подходом  ')
            elif message_name == '29':
                await message.answer(text='Элитарная культура '
                                          '\n1.	требует определенных знаний для понимания'
                                          '\n2.	ориентирована на определенную группу людей, ценителей '
                                          '\n3.	является способом самовыражения автора')
            elif message_name == '30':
                await message.answer(text='Массовая культура '
                                          '\n1.	коммерческий характер '
                                          '\n2.	развлекательный характер '
                                          '\n3.	ориентирована на среднего зрителя, легкость восприятия информации ')
            elif message_name == '31':
                await message.answer(text='Народная культура'
                                          '\n1.	передаётся устно '
                                          '\n2.	отражает национальный колорит народа '
                                          '\n3.	создается коллективным творчеством людей')
            elif message_name == '32':
                await message.answer(text='Реформа '
                                          '\n1.	не уничтожает основ существующего строя '
                                          '\n2.	целенаправленное преобразование какой-то определённой сферы общества '
                                          '\n3.	проводится государством ')
            elif message_name == '33':
                await message.answer(text='Революция '
                                          '\n1.	уничтожает основы существующего строя, полное изменение общественного строя  '
                                          '\n2.	обычно исходит от народа '
                                          '\n3.	влечет качественные изменения ')
            elif message_name == '34':
                await message.answer(text='Общественный прогресс'
                                          '\n1.	переход от низшего к высшему, от простого к сложному '
                                          '\n2.	противоречивость '
                                          '\n3.	относительность')
            elif message_name == '35':
                await message.answer(text='Традиционное общество '
                                          '\n1.	основной фактор производства-земля '
                                          '\n2.	натуральное хозяйство '
                                          '\n3.	сословная иерархия ')
            elif message_name == '36':
                await message.answer(text='Индустриальное общество '
                                          '\n1.	основной фактор производства-капитал  '
                                          '\n2.	массовое промышленное производство '
                                          '\n3.	появление массовой культуры ')
            elif message_name == '37':
                await message.answer(text='Постиндустриальное общество'
                                          '\n1.	основной фактор производства-информация '
                                          '\n2.	развитие наукоемких производств'
                                          '\n3.	выдвижение на первый план сферы услуг ')
            elif message_name == '38':
                await message.answer(text='Глобализация '
                                          '\n1.	процесс становления единого человечества '
                                          '\n2.	охватывает все сферы общества '
                                          '\n3.	противоречивый характер (положительные и отрицательные последствия)')
            elif message_name == '39':
                await message.answer(text='Глобальные проблемы человечества'
                                          '\n1.	решение проблемы возможно только совместным усилиями '
                                          '\n2.	затрагивают жизнедеятельность всего человечества, мировой масштаб '
                                          '\n3.	от их решения зависит судьба всего человечества ')
            else:
                await message.answer(text="Что-то странное ты ввел")

        await bot.answer_callback_query(callback_query.id, text='Нажата первая кнопка')
    elif code == 'menu_social_relations':
        await bot.send_message(chat_id=user_id,
                               text=text_social_relations)

        @dp.message_handler()
        async def social_relations(message: types.Message):
            user_id2 = message.from_user.id
            message_name = message.text
            user_full_name = message.from_user.full_name
            logging.info(f'{user_id2} {user_full_name} {time.asctime()} {message_name}')
            if message_name == '1':
                await message.answer(text="")

        await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
    elif code == 'menu_3':
        await bot.answer_callback_query(callback_query.id, text='Нажата третья кнопка')
    elif code == 'menu_4':
        await bot.answer_callback_query(callback_query.id, text='Нажата 4 кнопка')
    elif code == 'menu_5':
        await bot.answer_callback_query(
            callback_query.id,
            text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code} ')


@dp.message_handler(commands=['techsupport'])
async def techSupport(message: types.Message):
    await message.answer("Он во всем виноват - @Wam_Pan1")


@dp.message_handler(commands=['howtouse'])
async def howToUse(message: types.Message):
    await message.answer("тут должно быть про использование")


""""
@dp.message_handler()
async def echo(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    message_name = message.text
    logging.info(f'{user_id} {user_full_name} {time.asctime()} {message_name}')
    await message.answer(message.text)
"""

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# def text_for_human_and_society():
# сюда нужно запихнуть блоки ответов для меню(несколько функций)
