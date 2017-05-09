from db import get_all_messages, create_new
from load_manager import start_load


while True:
    result = input('Что мне сделать? >')
    if result == 'help':
        print('load - загрузить новые сообщения из социальных сетей')
        print('all - вывести все загруженные сообщения')
        print('clear - очистить базу данных или создать новую')
        print('exit - выход')
        print('help - вызов справки')
    elif result == 'load':
        start_load()
    elif result == 'clear':
        while True:
            result = input('Вы действительно хотите очистить/создать новую базу данных? ВСЕ ДАННЫЕ БУДУТ УДАЛЕНЫ. y/n ')
            if result.lower() == 'y':
                create_new()
                print('База данных успешно создана')
                break
            elif result.lower() == 'n':
                break
            else:
                print('Неверный ввод')
    elif result == 'all':
        messages = get_all_messages()
        count = 0
        for message in messages:
            count+=1
            print(message)
        print('Сообщений в базе: {}'.format(count))
    elif result == 'exit':
        break
    else:
        print('Неверная команда, для справки введит help')
